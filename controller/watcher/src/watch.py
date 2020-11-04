import time
import json
from threading import Thread

from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from web3.middleware import geth_poa_middleware

from control import servo_lock, servo_unlock

import tkinter
from PIL import Image, ImageTk

time.sleep(10)


def get_contract_address():
    try:
        with open('contracts/lock.json', 'r') as f:
            abi = json.load(f)
    except:
        print('cannot import abi')

    try:
        with open('contracts/tx_hash.txt', 'r') as f:
            tx_hash = f.read()
    except:
        ptint('cannot import tx_hash')

    try:
        infura_url = 'http://127.0.0.1:8545/'
        w3 = Web3(Web3.HTTPProvider(infura_url))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except:
        print('cannot load web3 instance')

    try:
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        contract_address = tx_receipt['contractAddress']
        contract = w3.eth.contract(address=contract_address, abi=abi)
        accounts = w3.eth.accounts
    except Exception as e:
        print('cannot load contract instance')
        print(e)

    return w3, contract, contract_address


def show_image():
    global item, canvas

    root = tkinter.Tk()
    root.attributes('-fullscreen', True)
    # root.bind('', lambda e: root.destroy())
    root.title('Status')
    root.geometry("1920x1080")
    img = Image.open('image/display_locked_qr.jpeg')
    img = ImageTk.PhotoImage(img)
    canvas = tkinter.Canvas(bg="black", width=1920, height=1080)
    canvas.place(x=0, y=0)
    item = canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
    root.mainloop()


def handle_event(w3, contract, event):
    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    locked = contract.events.Locked().processReceipt(receipt)
    if locked:
        img = Image.open('image/display_locked_qr.jpeg')
        img = ImageTk.PhotoImage(img)
        servo_lock()
        return img
        # print('locked')

    unlocked = contract.events.Unlocked().processReceipt(receipt)
    if unlocked:
        img2 = Image.open('image/display_unlocked_qr.jpeg')
        img2 = ImageTk.PhotoImage(img2)
        servo_unlock()
        return img2
        # print('unlocked')


def main():
    thread1 = Thread(target=show_image)
    thread1.start()

    w3, contract, contract_address = get_contract_address()
    event_filter = w3.eth.filter({'fromBlock': 'latest', 'address': contract_address})

    interval = 2
    while True:
        for event in event_filter.get_new_entries():
            print(event)
            img = handle_event(w3, contract, event)
            canvas.itemconfig(item, image=img)
            time.sleep(interval)


if __name__ == '__main__':
    main()
