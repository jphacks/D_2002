// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Lock {
    bool private is_lock = false;

    event Locked (
        address indexed _from
    );

    function lock() public {
        is_lock = true;
        emit Locked(msg.sender);
    }

    event Unlocked (
        address indexed _from
    );

    function unlock() public {
        is_lock = false;
        emit Unlocked(msg.sender);
    }

    function status() public view returns (bool) {
        return is_lock;
    }
}