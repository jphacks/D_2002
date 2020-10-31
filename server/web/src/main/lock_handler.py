from web3 import Web3
from web3.contract import ConciseContract
from web3.middleware import geth_poa_middleware
import json

try:
    with open('static/contract_info/abi', 'r') as f:
        abi = json.load(f)
    with open('static/contract_info/tx_hash.txt', 'r') as f:
        tx_hash = f.read()

        infura_url = 'http://geth:8545'
        w3 = Web3(Web3.HTTPProvider(infura_url))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
        contract_address = tx_receipt['contractAddress']
        contract_instance = w3.eth.contract(abi=abi, address=contract_address, ContractFactoryClass=ConciseContract)

except Exception as e:
    print(e)

def get_status():
    status = 'Locked' if contract_instance.status() else 'Unlocked'
    return status


def unlock():
    contract_instance.unlock(transact={'from': w3.eth.accounts[0]})
    return "unlocked"


def lock():
    contract_instance.lock(transact={'from': w3.eth.accounts[0]})
    return "locked"
