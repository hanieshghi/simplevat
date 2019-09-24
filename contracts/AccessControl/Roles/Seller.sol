pragma solidity ^0.5.0;

/// Import the 'Roles' library from OpenZeppelin contracts package
import "../../openzeppelin/contracts/access/Roles.sol";


/// @author Khalid F.Sh
/// @title A Seller Role Contract
/// @dev contract for adding, removing and checking an address in the container '_Sellers' Role.
/// @notice functionalty in this contract are internal to be managed in './Rolable.sol' contract.
contract Seller {

    /// using Role struct from 'Roles' library
    using Roles for Roles.Role;

    /// 2 events, one for Adding, and other for Removing
    event SellerAdded(address indexed account);
    event SellerRemoved(address indexed account);

    /// structure '_Sellers' inherited from 'Roles' library
    Roles.Role private _Sellers;

    /// @notice constructer will assign the deployer as 1st Seller
    constructor () internal {
        _addSeller(msg.sender);
    }

    // modifier that checks to see if `msg.sender` has Seller role
    modifier onlySeller() {
        require(isSeller(msg.sender), 'Not A Seller!');
        _;
    }

    /// Function to check even he has Seller role or not
    /// @param account address to be checked
    /// @return boolean for this address state in `_Sellers` Role
    /// @notice uses'Roles' library's internal function `has()` to check, refer to library for more detail
    function isSeller(address account) public view returns (bool) {
        return _Sellers.has(account);
    }

    /// Function to check caller `msg.sender` if he has Seller role
    /// @return boolean for caller address state in `_Sellers` Role
    function amISeller() public view returns (bool) {
        return _Sellers.has(msg.sender);
    }

    /// Function to assign caller `msg.sender` to Seller role
    function assignMeAsSeller() public {
        _addSeller(msg.sender);
    }

    /// Function to renounce caller `msg.sender` from Seller role
    function renounceMeFromSeller() public {
        _removeSeller(msg.sender);
    }

    /// Internal function to add account to this role
    /// @param account address to be Added
    /// @notice uses'Roles' library's internal function `add()`, refer to the library for more detail
    function _addSeller(address account) internal {
        _Sellers.add(account);
        emit SellerAdded(account);
    }

    /// Internal function to remove account from this role
    /// @param account address to be removed
    /// @notice uses'Roles' library's internal function `remove()`, refer to the library for more detail
    function _removeSeller(address account) internal {
        _Sellers.remove(account);
        emit SellerRemoved(account);
    }
}
