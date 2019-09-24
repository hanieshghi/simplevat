pragma solidity ^0.5.0;

contract Product {

    uint pID;

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


    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isProductTaxTracked(uint _pID) {
        require(pItems[_pID].taxUpdateCounter != 0);
        _;
    }

    /// Constructor Function sets up pID and pID to 0
    constructor() public {
        pID = 0;
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
        updateTaxHistory(_pID , _tax);
        //newProductItem.taxHistory[0].totalTax = _tax;
        //newProductItem.taxHistory[0].lastPaidTax = _tax;
        /*for (uint i = 0; i < quantity; i++) {
            uint _pID = ++pID;
            newProductItem.pID = _pID;
            pItems[_pID] = newProductItem;
            
            stockLouds[_pID].push(_pID);
        }*/
        pItems[_pID] = newProductItem;
        emit Manufactured(_pID);
    }

    function purchaseProduct (uint _pID)
        public
        payable
        isProductTaxTracked(_pID)
    {
        pItems[_pID].state = ProductState.Purchased;
        pItems[_pID].currentOwnerId = msg.sender;

        emit Purchased(_pID);
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
            uint numberOfTaxUpdate
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
        totalTax = _ProductItem.taxHistory[numberOfTaxUpdate].totalTax;
        lastPaidTax = _ProductItem.taxHistory[numberOfTaxUpdate].lastPaidTax;
    }


    function updateTaxHistory (
        uint _pID,
        uint _paidTax
        //uint _totalTax
    )
        public
    {   
        uint _totalTax;
        if(pItems[_pID].taxUpdateCounter == 0){
            _totalTax = pItems[_pID].taxHistory[pItems[_pID].taxUpdateCounter].totalTax + _paidTax;
        }
        else{
            _totalTax = pItems[_pID].taxHistory[pItems[_pID].taxUpdateCounter-1].totalTax + _paidTax; 
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
        external
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
