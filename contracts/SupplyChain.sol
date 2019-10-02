pragma solidity ^0.5.0;

/// Import main chains contracts
import "./Product.sol";
//import "./ProductDesign.sol";

/// Import Main Roles contract `Rolable.sol`
import "./AccessControl/Rolable.sol";

/// Import Pausable contract from OpenZeppelin library
import "./openzeppelin/contracts/lifecycle/Pausable.sol";

/// @title Supply Chain Contract
contract SupplyChain is Rolable, Pausable, Product {
    address payable public taxCollector = 0xaC9cEF7d952a26b75777aB191213073cdB987Adb;//ACount3;
    constructor() public {

    }

    function manufacturProductsLoud(uint _price, uint _tax, string memory _name)
        public
        //onlyManufacturer()
    {
        super.manufacturProductsLoud(_price, _tax, _name);
    }
    
    function updateTaxHistory(uint _pID, uint _paidTax)
        public
        //onlyManufacturer()
    {
        super.updateTaxHistory( _pID, _paidTax);
    }
    

    /// Function helps manufacturer to Pack a isManufactured Product Loud
    function purchaseProduct (uint _pID)
        public
        payable
        //onlyBuyer()
        whenNotPaused()
    {
        uint price = pItems[_pID].price;
        address payable sellerId = pItems[_pID].currentOwnerId;

        //address payable retailerId = address(uint160(pItems[_pID].sellerId));
        //uint retialerBounty = (price*5) /100;
        uint lastTax = pItems[_pID].taxHistory[pItems[_pID].taxUpdateCounter-1].lastPaidTax ; 
        uint taxBounty = (price*9) /100 - lastTax ; 

        require(msg.value >= price+(price*9) /100, "Not Enough!");
        uint amountToReturn = msg.value - (price + lastTax + taxBounty);
        if (amountToReturn != 0)
            address(msg.sender).transfer(amountToReturn);

        super.purchaseProduct(_pID);
        updateTaxHistory(_pID,taxBounty);
        sellerId.transfer(price + lastTax);
        taxCollector.transfer(taxBounty);
    }

}
