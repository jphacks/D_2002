import os
import json
import configparser

from web3 import Web3
from web3.contract import ConciseContract
from web3.middleware import geth_poa_middleware

from .models import Product


class ContractManager:
    def __init__(self):
        self.infura_url = 'http://geth:8545'
        self.abi_path = 'static/contracts/lock_abi.json'
        self.bytecode_path = 'static/contracts/lock_bytecode.json'
        self.tx_hash_path = 'static/contracts/tx_hash.txt'

        self.abi = self.get_abi()
        self.bytecode = self.get_bytecode()
        self.tx_hash = self.get_tx_hash()
        self.web3_instance = self.get_web3_instance()
        self.contract_instance = self.get_contract_instance()

    def get_abi(self):
        try:
            with open(self.abi_path, 'r') as f:
                abi = json.load(f)
        except Exception:
            print('cannot import abi')
            abi = ''

        return abi
        
    def get_bytecode(self):
        try:
            with open(self.bytecode_path) as f:
                bytecode = json.load(f)
            bytecode = bytecode['object']
        except Exception:
            print('caanot import bytecode')
            bytecode = ''

        return bytecode

    def get_tx_hash(self):
        try:
            tx_hash = Product.objects.last().tx_hash 
        except Exception:
            print('cannot import tx_hash')
            tx_hash = ''

        return tx_hash
        
    def deploy_contract(self, value):
        try:
            contract = self.web3_instance.eth.contract(abi=self.abi, bytecode=self.bytecode)
            self.tx_hash = contract.constructor(value).transact().hex()
            tx_recipt = self.web3_instance.eth.waitForTransactionReceipt(self.tx_hash)
            self.contract_instance = self.web3_instance.eth.contract(
                abi=self.abi,
                address=tx_receipt['contractAddress'],
                ContractFactoryClass=ConciseContract
            )
        except Exception as e:
            print('cannot send transaction')
            print(e)
        
        return self.tx_hash

    def get_web3_instance(self):
        try:
            w3 = Web3(Web3.HTTPProvider(self.infura_url))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            w3.eth.defaultAccount = w3.eth.accounts[0]
        except Exception:
            print('cannot load web3 instance')
            w3 = ''

        return w3

    def get_contract_instance(self):
        try:
            tx_receipt = self.web3_instance.eth.getTransactionReceipt(self.tx_hash)
            contract_address = tx_receipt['contractAddress']
            contract_instance = self.web3_instance.eth.contract(
                abi=self.abi,
                address=contract_address,
                ContractFactoryClass=ConciseContract
            )
        except Exception:
            print('cannot load contract instance')
            contract_instance = ''

        return contract_instance

    def get_status(self):
        try:
            status = 'Locked' if self.contract_instance.is_lock() else 'Unlocked'
        except Exception:
            status = 'Unknown'

        return status

    def unlock(self):
        try:
            self.contract_instance.unlock(transact={'from': self.web3_instance.eth.accounts[1], 'value': self.get_price()})
        except Exception:
            print('cannoot unlock')

        return "unlocked"

    def lock(self):
        try:
            self.contract_instance.lock(transact={'from': self.web3_instance.eth.accounts[0]})
        except Exception:
            print('cannot lock')

        return "locked"
    
    def get_price(self):
        try:
            price = self.contract_instance.price() 
        except Exception:
            price = 1000

        return price
