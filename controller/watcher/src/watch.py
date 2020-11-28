import io
import json
import os
import subprocess
import time
import tkinter
import urllib.request
from threading import Thread

import requests
from PIL import Image, ImageTk
from web3 import Web3
from web3.logs import DISCARD, IGNORE, STRICT, WARN
from web3.middleware import geth_poa_middleware

from control import servo_lock, servo_unlock
from senser import get_data


is_locked = True

def show_image():
    global canvas, item, show_img

    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    # root.bind('', lambda e: root.destroy())
    root.title('Status')
    root.geometry("1920x1080")
    img = Image.open('image/display_starting.jpeg')
    show_img = ImageTk.PhotoImage(img)
    
    canvas = tkinter.Canvas(bg="black", width=1920, height=1080)
    canvas.place(x=0, y=0)
    item = canvas.create_image(0, 0, image=show_img, anchor=tkinter.NW)
    root.mainloop()


def test_play_voice(text):
    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', '/usr/share/hts-voice/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'output.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    while True:
        subprocess.run(cmd, input=text.encode())
        aplay = ['aplay', '-q', 'output.wav']
        wr = subprocess.Popen(aplay)
        wr.wait()


def play_voice():
    global intro_text, is_detect, is_locked

    open_jtalk = ['open_jtalk']
    mech = ['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice = ['-m', '/usr/share/hts-voice/mei_normal.htsvoice']
    speed = ['-r', '1.0']
    outwav = ['-ow', 'output.wav']
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    pre_text = ''
    
    while True:
        try:
            if is_detect:
                if pre_text != intro_text:
                    print(intro_text)
                    pre_text = intro_text
                    subprocess.run(cmd, input=intro_text.encode())
                if intro_text and is_locked:
                    aplay = ['aplay', '-q', 'output.wav']
                    wr = subprocess.Popen(aplay)
                    wr.wait()
        except Exception as e:
            print(e)


def get_sensor_data():
    global is_detect
    
    while True:
        is_detect = get_data()
        time.sleep(2)

def get_contract_address():
    global canvas, item, show_img, intro_text
    try:
        with open('contracts/lock.json', 'r') as f:
            abi = json.load(f)
    except:
        print('cannot import abi')

    # apiからデータを取得
    try:
        url = "http://192.168.10.10:8080/api/products"
        products_get = requests.get(url)
        product_dict = products_get.json()[-1] #最新のレコードを辞書型で取得
    except Exception as e:
        print('cannot connect to the dataset api')

    #tx_hashを取得
    try:
        tx_hash = product_dict['tx_hash']
    except:
        tx_hash = ''
        print('cannot get tx_hash')
        
    # 紹介文を取得
    try:
        intro_text = product_dict['intro']
    except:
        intro_text = ''
        print('cannot get introduction')

    #imageのURLを取得
    try:        
        image_url = product_dict['image']
        img_read = urllib.request.urlopen(image_url).read()
        img_bin = io.BytesIO(img_read)
        img = Image.open(img_bin)
        tmp_img = ImageTk.PhotoImage(img)
        if show_img != tmp_img and is_locked:
            canvas.itemconfig(item, image=tmp_img)
            show_img = tmp_img
    except Exception as e:
        image_url = ''
        print('cannot get image_url')

    try:
        infura_url = 'http://geth:8545/'
        w3 = Web3(Web3.HTTPProvider(infura_url))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except:
        w3 = ''
        print('cannot load web3 instance')

    try:
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        contract_address = tx_receipt['contractAddress']
        contract = w3.eth.contract(address=contract_address, abi=abi)
        accounts = w3.eth.accounts
    except Exception as e:
        contract_address = ''
        contract = ''
        print('cannot load contract instance')

    return w3, contract, contract_address, image_url
        

def search_contract():
    global w3, contract, contract_address, image_url

    while True:
        w3, contract, contract_address, image_url = get_contract_address()
        time.sleep(2)


def handle_event(event):
    global canvs, item, show_img, image_url, is_locked
    
    receipt = w3.eth.getTransactionReceipt(event['transactionHash'])
    locked = contract.events.Locked().processReceipt(receipt)
    if locked:
        try:
            img_read = urllib.request.urlopen(image_url).read()
            img_bin = io.BytesIO(img_read)
            img = Image.open(img_bin)
            show_img = ImageTk.PhotoImage(img)
            canvas.itemconfig(item, image=show_img)
            is_locked = True
            servo_lock()
        except Exception as e:
            img = Image.open('image/display_locked_qr_demo.jpeg')
            show_img = ImageTk.PhotoImage(img)
            canvas.itemconfig(item, image=show_img)
            servo_lock()
            print(e)
        # print('locked')

    unlocked = contract.events.Unlocked().processReceipt(receipt)
    if unlocked:
        img = Image.open('image/display_unlocked_qr_demo.jpeg')
        show_img = ImageTk.PhotoImage(img)
        canvas.itemconfig(item, image=show_img)
        is_locked = False
        servo_unlock()
        # print('unlocked')


def get_event():
    global w3, contract_address
    interval = 2
    while True:
        try:
            event_filter = w3.eth.filter({'fromBlock': 'latest', 'address': contract_address})
            while True:
                for event in event_filter.get_new_entries():
                    print(event)
                    handle_event(event)
                    time.sleep(interval)
        except Exception as e:
            print(f'{e} => search next event')
        time.sleep(interval)
        

def main():
    thread1 = Thread(target=show_image)
    thread1.start()
    
    thread2 = Thread(target=search_contract)
    thread2.start()
    
    thread3 = Thread(target=play_voice)
    thread3.start()
    
    thread4 = Thread(target=get_sensor_data)
    thread4.start()
    
    thread5 = Thread(target=get_event)
    thread5.start()


if __name__ == '__main__':
    main()
