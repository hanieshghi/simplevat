pragma solidity ^0.5.0;

import "../../openzeppelin/contracts/access/Roles.sol";

contract Buyer {

    using Roles for Roles.Role;

    event BuyerAdded(address indexed account);
    event BuyerRemoved(address indexed account);

    /// structure '_Buyers' inherited from 'Roles' library
    Roles.Role private _Buyers;

    /// @notice constructer will assign the deployer as 1st Buyer
    constructor () internal {
        _addBuyer(msg.sender);
    }

    // modifier that checks to see if `msg.sender` has Buyer role
    modifier onlyBuyer() {
        require(isBuyer(msg.sender), 'Not A Buyer!');
        _;
    }

    /// Function to check even he has Buyer role or not
    /// @param account address to be checked
    /// @return boolean for this address state in `_Buyers` Role
    /// @notice uses'Roles' library's internal function `has()` to check, refer to library for more detail
    function isBuyer(address account) public view returns (bool) {
        return _Buyers.has(account);
    }

    /// Function to check caller `msg.sender` if he has Buyer role
    /// @return boolean for caller address state in `_Buyers` Role
    function amIBuyer() public view returns (bool) {
        return _Buyers.has(msg.sender);
    }

    /// Function to assign caller `msg.sender` to Buyer role
    function assignMeAsBuyer() public {
        _addBuyer(msg.sender);
    }

    /// Function to renounce caller `msg.sender` from Buyer role
    function renounceMeFromBuyer() public {
        _removeBuyer(msg.sender);
    }

    /// Internal function to add account to this role
    /// @param account address to be Added
    /// @notice uses'Roles' library's internal function `add()`, refer to the library for more detail
    function _addBuyer(address account) internal {
        _Buyers.add(account);
        emit BuyerAdded(account);
    }

    /// Internal function to remove account from this role
    /// @param account address to be removed
    /// @notice uses'Roles' library's internal function `remove()`, refer to the library for more detail
    function _removeBuyer(address account) internal {
        _Buyers.remove(account);
        emit BuyerRemoved(account);
    }
}
