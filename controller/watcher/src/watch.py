import time
import json
from threading import Thread

from web3 import Web3
from web3.logs import STRICT, IGNORE, DISCARD, WARN
from web3.middleware import geth_poa_middleware

from control import servo_lock, servo_unlock

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

def handle_event(event):
    receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
    locked = contract.events.Locked().processReceipt(receipt)
    if locked:
        servo_lock()
        # print('locked')
    unlocked = contract.events.Unlocked().processReceipt(receipt)
    if unlocked:
        servo_unlock()
        # print('unlocked')

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            print(event)
            handle_event(event)
            time.sleep(poll_interval)

block_filter = w3.eth.filter({'fromBlock':'latest', 'address':contractAddress})
log_loop(block_filter, 2)