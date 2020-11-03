import time
import json
from threading import Thread

from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from web3.middleware import geth_poa_middleware

from control import servo_lock, servo_unlock

import tkinter
from PIL import Image, ImageTk

###############################################################################
# Web3 関連
###############################################################################
with open('abi', 'r') as f:
    abi = json.load(f)

infura_url = 'http://geth:8545'
tx_hash = "0xe5ae65b502bdea31300f3e1e5127428829a78b578cca343d914fd4c1a09d3a9a"

w3 = Web3(Web3.HTTPProvider(infura_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contractAddress = tx_receipt['contractAddress']
contract = w3.eth.contract(address=contractAddress, abi=abi)
accounts = w3.eth.accounts
###############################################################################


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


def handle_event(event):
    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    locked = contract.events.Locked().processReceipt(receipt)
    if locked:
        img = Image.open('image/display_locked_qr.jpeg')
        img = ImageTk.PhotoImage(img)
        canvas.itemconfig(item, image=img)
        servo_lock()
        # print('locked')

    unlocked = contract.events.Unlocked().processReceipt(receipt)
    if unlocked:
        img2 = Image.open('image/display_unlocked_qr.jpeg')
        img2 = ImageTk.PhotoImage(img2)
        canvas.itemconfig(item, image=img2)
        servo_unlock()
        # print('unlocked')


def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            print(event)
            handle_event(event)
            time.sleep(poll_interval)


thread1 = Thread(target=show_image)
thread1.start()

block_filter = w3.eth.filter({'fromBlock': 'latest', 'address': contractAddress})
log_loop(block_filter, 2)
