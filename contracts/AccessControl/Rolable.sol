pragma solidity ^0.5.0;

/// Import all Roles
import "./Roles/Buyer.sol";
import "./Roles/Designer.sol";
import "./Roles/Seller.sol";
import "./Roles/Manufacturer.sol";


contract Rolable is Buyer, Designer, Seller{

    /// Function to check all roles for the caller
    /// @return array contining every role with its state as boolean
    function whoAmI() public view returns(
        bool Buyer,
        bool Seller,
        bool manufacturer,
        bool designer
    )
    {
        Buyer = amIBuyer();
        Seller = amISeller();
        manufacturer = amIManufacturer();
        designer = amIDesigner();
    }
}
