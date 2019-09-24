pragma solidity ^0.5.0;

/// Import main chains contracts
import "./Product.sol";
import "./ProductDesign.sol";

/// Import Main Roles contract `Rolable.sol`
import "./AccessControl/Rolable.sol";

/// Import Pausable contract from OpenZeppelin library
import "./openzeppelin/contracts/lifecycle/Pausable.sol";

/// @title Supply Chain Contract
contract SupplyChain is Rolable, Pausable, ProductDesign, Product {
    address payable public taxCollector  ;
    constructor() public {

    }

    /// Function helps Designer to estaplish a new Product Design
    function designProduct(
        string memory _designerName,
        string memory _ProductName,
        string memory _description,
        string memory _notes
    )
        public
        onlyDesigner()
        whenNotPaused()
    {
        super.designProduct(
            _designerName,
            _ProductName,
            _description,
            _notes
        );
    }


    /// Function to purchase a Product design
    function purchaseProductDesign(uint _udpc)
        public
        payable
        onlyManufacturer()
    {
        super.purchaseProductDesign(_udpc);
    }

    /// Function helps manufacturer to manufactur a new Product Loud
    function manufacturProductsLoud(uint _udpc, uint quantity)
        public
        onlyManufacturer()
    {
        super.manufacturProductsLoud(_udpc, quantity);
    }



    function buyProductsLoud(uint _slu)
        public
        payable
        onlyBuyer() // خریدار عمده
        whenNotPaused()
    {
        /// collect info about the whole proccess
        ProductItem storage sampleUnit = pItems[stockLouds[_slu][0]];
        //uint _udpc = sampleUnit.udpc;
        uint price = sampleUnit.price;
        uint quantity = stockLouds[_slu].length;
       // uint totalPrice = price*quantity;
        
        uint lastTax = sampleUnit.taxHistory[sampleUnit.taxUpdateCounter].lastPaidTax ; 
        uint taxBounty = (price*9) /100 - lastTax ;

        uint totalPrice = (price+ (price*9) /100 )*quantity;
        uint totalTaxBounty = taxBounty * quantity;
        ///colect shared worker addresses to payed them
        address payable sallerId = address(sampleUnit.currentOwnerId);

        require(msg.value >= totalPrice, "Not Enough!");
        uint amountToReturn = msg.value - totalPrice;
        if (amountToReturn != 0)
            address(msg.sender).transfer(amountToReturn);

        super.buyProductsLoud(_slu);
        super.updateTaxHistory(_slu,taxBounty);
        sallerId.transfer(totalPrice - totalTaxBounty);
        taxCollector.transfer(totalTaxBounty);
        
    }

    /// Function helps manufacturer to Pack a isManufactured Product Loud
    function purchaseProduct (uint _pku)
        public
        payable
        onlyBuyer()
        whenNotPaused()
    {
        uint price = pItems[_pku].price;
        address payable sellerId = pItems[_pku].currentOwnerId;

        //address payable retailerId = address(uint160(pItems[_pku].sellerId));
        //uint retialerBounty = (price*5) /100;
        uint lastTax = pItems[_pku].taxHistory[pItems[_pku].taxUpdateCounter].lastPaidTax ; 
        uint taxBounty = (price*9) /100 - lastTax ; 

        require(msg.value >= price+(price*9) /100, "Not Enough!");
        uint amountToReturn = msg.value - price;
        if (amountToReturn != 0)
            address(msg.sender).transfer(amountToReturn);

        super.purchaseProduct(_pku);
        //super.updateTaxHistory(_pku,taxBounty);
        sellerId.transfer(price + lastTax);
        taxCollector.transfer(taxBounty);
    }

}
