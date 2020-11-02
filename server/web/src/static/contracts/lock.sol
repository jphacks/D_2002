// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;


contract Lock {
    bool public is_lock;
    uint public price;
    address payable public seller;
    address public buyer;
    
    constructor(uint _price) {
        seller = msg.sender;
        price = _price;
        is_lock = true;
    }
    
    modifier condition(bool _condition) {
        require(_condition);
        _;
    }
    
    event Locked();
    
    function lock() public {
        emit Locked();
        is_lock = true;
    }

    event Unlocked();
    
    function unlock() public condition(msg.value == price) payable {
        emit Unlocked();
        is_lock = false;
        buyer = msg.sender;
        seller.transfer(msg.value);
    }
}