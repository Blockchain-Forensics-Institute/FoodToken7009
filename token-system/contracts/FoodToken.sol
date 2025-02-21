// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FoodToken is ERC20, Ownable {
    mapping(address => bool) public registeredUsers;
    mapping(address => bool) public vendors;

    event UserRegistered(address indexed user);
    event VendorRegistered(address indexed vendor);
    event TokenIssued(address indexed user, uint256 amount);
    event TokenRedeemed(address indexed user, address indexed vendor, uint256 amount);

    constructor() ERC20("FoodToken", "FTK") Ownable(msg.sender) {}

    function registerUser(address user, uint256 amount) external {
        require(!registeredUsers[user], "User already registered");
        registeredUsers[user] = true;
        _mint(user, amount);
        emit UserRegistered(user);
        emit TokenIssued(user, amount);
    }

    function registerVendor(address vendor) external onlyOwner {
        require(!vendors[vendor], "Vendor already registered");
        vendors[vendor] = true;
        emit VendorRegistered(vendor);
    }

    function redeemTokens(address vendor, uint256 amount) external {
        require(vendors[vendor], "Vendor not registered");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _transfer(msg.sender, vendor, amount);
        emit TokenRedeemed(msg.sender, vendor, amount);
    }
}
