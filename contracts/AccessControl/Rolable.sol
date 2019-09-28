pragma solidity ^0.5.0;

/// Import all Roles
import "./Roles/Buyer.sol";
import "./Roles/Manufacturer.sol";


contract Rolable is Buyer,Manufacturer{

    /// Function to check all roles for the caller
    /// @return array contining every role with its state as boolean
    function whoAmI() public view returns(
        bool Buyer,
        bool manufacturer
    )
    {
        Buyer = amIBuyer();
        manufacturer = amIManufacturer();
    }
}
