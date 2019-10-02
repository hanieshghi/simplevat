pragma solidity ^0.5.0;

contract Product {

    uint pID;
    uint counter = 0;
    mapping (uint => ProductItem) pItems;

    enum ProductState {
        Manufactured,
        Purchased
    }

    // Structure for Envirument update unit
    struct TaxUpdateOpj {
        uint timeStamp;
        uint lastPaidTax;
        uint totalTax;
        address updaterAddress;
    }

    /// Structure for keeping Product Design fields structured
    struct ProductItem {

        string name;
        uint pID;
        ProductState state;
        address payable currentOwnerId;
        address manufacturerId;
        uint price;
        mapping(uint => TaxUpdateOpj) taxHistory;
        uint taxUpdateCounter;
        bool customerRecieved;
    }

    /// Event to emit them for users in functions, accept `pID` as input as stock expected
    event Manufactured(uint pID);
    event taxUpdated(uint pID);
    //event Sold(uint pID);
    /// Event to emit them for users in functions, accept `pID` as input as one product unit expected
    event Purchased(uint pID);

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isManufactured(uint _pID) {
        //uint firstpID = stockLouds[_pID][0];
        require(pItems[_pID].state == ProductState.Manufactured);
        _;
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isTaxTracked(uint _pID) {
        //uint firstpID = stockLouds[_pID][0];
        require(pItems[_pID].taxUpdateCounter != 0);
        _;
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier onlyManufacturerOf(uint _pID) {
        //uint firstpID = stockLouds[_pID][0];
        bool isManuf = pItems[_pID].manufacturerId == msg.sender;
        require(isManuf);
        _;
    }

    modifier onlyOwnerOf(uint _pID) {
        //uint firstpID = stockLouds[_pID][0];
        bool isOwner = pItems[_pID].currentOwnerId == msg.sender;
        require(isOwner);
        _;
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isProductTaxTracked(uint _pID) {
        require(pItems[_pID].taxUpdateCounter != 0);
        _;
    }

    modifier isNotCustomerRecieved(uint _pID){
        require(pItems[_pID].customerRecieved != true);
        _;
    }
    /// Constructor Function sets up pID and pID to 0
    constructor() public {
        pID = 0;
    }

    /// Function helps manufacturer to manufactur a new Product Loud
    function manufacturProductsLoud(uint _price, uint _tax, string memory _name) public {
        uint _pID = ++pID;
        ProductItem memory newProductItem;
        //newProductItem.udpc = _udpc;
        newProductItem.pID = _pID;
        newProductItem.state = ProductState.Manufactured;
        newProductItem.currentOwnerId = msg.sender;
        newProductItem.manufacturerId = msg.sender;
        newProductItem.taxUpdateCounter = 0;
        newProductItem.price = _price;
        newProductItem.name = _name;
        newProductItem.customerRecieved = false;
        pItems[_pID] = newProductItem;
        updateTaxHistory(_pID , _tax);
        counter++;
        //newProductItem.taxUpdateCounter = pItems[_pID].taxUpdateCounter ;
        emit Manufactured(_pID);
    }

    function purchaseProduct (uint _pID)
        public
        payable
        isProductTaxTracked(_pID)
        isNotCustomerRecieved(_pID)
    {
        pItems[_pID].state = ProductState.Purchased;
        pItems[_pID].currentOwnerId = msg.sender;

        emit Purchased(_pID);
    }
    
    function setNewPrice(uint _pID,uint newPrice) public onlyOwnerOf(_pID){
        require( _pID != 0, 'Given pID Not Created Yet!');
        pItems[_pID].price = newPrice;
    }

    function setCustomerRecieved(uint _pID) public onlyOwnerOf(_pID){
        require( _pID != 0, 'Given pID Not Created Yet!');
        pItems[_pID].customerRecieved = true;
    }

    function getCustomerRecieved(uint _pID) public view returns(bool){
        require( _pID != 0, 'Given pID Not Created Yet!');
        return (pItems[_pID].customerRecieved);
    }

    function getLastPID() public view returns(uint){
        return counter ;
    }

    function fetchProductItemData(uint _pID)
        public
        view
        returns(
            //uint _udpc,
            uint pID,
            string memory name,
            address currentOwner,
            address manufacturerId,
            uint price,
            uint totalTax,
            uint lastPaidTax,
            uint numberOfTaxUpdate,
            bool customerRecieved
        )
    {
        require( _pID != 0, 'Given pID Not Created Yet!');
        ProductItem  storage _ProductItem = pItems[_pID];
        pID = _pID;
        name = _ProductItem.name;
        currentOwner = _ProductItem.currentOwnerId;
        manufacturerId = _ProductItem.manufacturerId;
        price = _ProductItem.price;
        numberOfTaxUpdate = _ProductItem.taxUpdateCounter;
        totalTax = _ProductItem.taxHistory[numberOfTaxUpdate-1].totalTax;
        lastPaidTax = _ProductItem.taxHistory[numberOfTaxUpdate-1].lastPaidTax;
        customerRecieved = _ProductItem.customerRecieved;
    }


    function updateTaxHistory(
        uint _pID,
        uint _paidTax
        //uint _totalTax
    )
        public
    {   
        uint _totalTax;
        if(pItems[_pID].taxUpdateCounter == 0){
            _totalTax = _paidTax;
        }
        else if(pItems[_pID].taxUpdateCounter != 0){
            _totalTax = pItems[_pID].taxHistory[pItems[_pID].taxUpdateCounter - 1].totalTax + _paidTax; 
        }
        
        
        TaxUpdateOpj memory _taxUpdate = TaxUpdateOpj(
            now,
            _paidTax,
            _totalTax,
            msg.sender
        );
        //for (uint i = 0; i < quantity; i++) {
            //uint _pID = stockLouds[_pID][i];

        pItems[_pID].taxHistory[pItems[_pID].taxUpdateCounter] = _taxUpdate;
        pItems[_pID].taxUpdateCounter ++;
       // }
        emit taxUpdated(_pID);
      
    }




    function fetchtaxHistory(uint _pID)
        public
        view
        isProductTaxTracked(_pID)
        returns(
            uint numberOfupdate,
            uint[] memory timeStamps,
            uint[] memory lastPaidTax,
            uint[] memory totalTax,
            address[] memory updaterAddresses
        )
    {
        ProductItem  storage _ProductItem = pItems[_pID];
        numberOfupdate = _ProductItem.taxUpdateCounter;
        uint[] memory _timeStamps = new uint[](numberOfupdate);
        uint[] memory _lastPaidTax = new uint[](numberOfupdate);
        uint[] memory _totalTax = new uint[](numberOfupdate);
        address[] memory _updaterAddresses = new address[](numberOfupdate);
        for (uint i = 0; i < _ProductItem.taxUpdateCounter; i++) {
            TaxUpdateOpj storage _taxUpdate = _ProductItem.taxHistory[i];
            _timeStamps[i] = _taxUpdate.timeStamp;
            _lastPaidTax[i] = _taxUpdate.lastPaidTax;
            _totalTax[i] = _taxUpdate.totalTax;
            _updaterAddresses[i] = _taxUpdate.updaterAddress;
        }
        (timeStamps, lastPaidTax, totalTax, updaterAddresses) = (
            _timeStamps, 
            _lastPaidTax, 
             _totalTax,
            _updaterAddresses
        );
    }

}
