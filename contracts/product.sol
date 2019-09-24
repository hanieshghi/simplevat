pragma solidity ^0.5.0;

contract Product {

    /// Variable for tracking Product Kepping Unit (PKU)
    uint pku;

    /// Variable for tracking Stock Louding Uint (SLU)
    uint slu;

    /// Public mapping from PKU to a Product Item
    mapping (uint => ProductItem) pItems;

    /// Public mapping from SLU to a array of PKU
    mapping (uint => uint[]) stockLouds;

    // Enumaration for defining variety of Product State
    enum ProductState {
        Manufactured,
        NotPurchasedYet,
        Purchased
    }

    // Structure for Envirument update unit
    struct TaxUpdateOpj {
        uint timeStamp;
        uint lastPaidTax;
        //uint totalTax;
        address updaterAddress;
    }

    /// Structure for keeping Product Design fields structured
    struct ProductItem {
        uint udpc;
        uint pku;
        uint slu;
        ProductState state;
        address payable currentOwnerId;
        address manufacturerId;
        //address sellerId;
        uint price;
        mapping(uint => TaxUpdateOpj) taxHistory;
        uint taxUpdateCounter;
    }

    /// Event to emit them for users in functions, accept `slu` as input as stock expected
    event Manufactured(uint slu);
    event taxUpdated(uint slu);
    event Sold(uint slu);
    /// Event to emit them for users in functions, accept `pku` as input as one product unit expected
    event Purchased(uint pku);

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isManufactured(uint _slu) {
        uint firstPKU = stockLouds[_slu][0];
        require(pItems[firstPKU].state == ProductState.Manufactured);
        _;
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isTaxTracked(uint _slu) {
        uint firstPKU = stockLouds[_slu][0];
        require(pItems[firstPKU].taxUpdateCounter != 0);
        _;
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier onlyManufacturerOf(uint _slu) {
        uint firstPKU = stockLouds[_slu][0];
        bool isManuf = pItems[firstPKU].manufacturerId == msg.sender;
        require(isManuf);
        _;
    }


    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isProductTaxTracked(uint _pku) {
        require(pItems[_pku].taxUpdateCounter != 0);
        _;
    }

    /// Constructor Function sets up SLU and PKU to 0
    constructor() public {
        slu = 0;
        pku = 0;
    }

    /// Function helps manufacturer to manufactur a new Product Loud
    function manufacturProductsLoud(uint _udpc, uint quantity) public {
        uint _slu = ++slu;
        ProductItem memory newProductItem;
        newProductItem.udpc = _udpc;
        newProductItem.slu = _slu;
        newProductItem.state = ProductState.Manufactured;
        newProductItem.currentOwnerId = msg.sender;
        newProductItem.manufacturerId = msg.sender;
        newProductItem.taxUpdateCounter = 0;
        for (uint i = 0; i < quantity; i++) {
            uint _pku = ++pku;
            newProductItem.pku = _pku;
            pItems[_pku] = newProductItem;
            
            stockLouds[_slu].push(_pku);
        }
        emit Manufactured(_slu);
    }

    function buyProductsLoud(uint _slu)
        public
        payable
        {
        uint quantity = stockLouds[_slu].length;
        for (uint i = 0; i < quantity; i++) {
            uint _pku = stockLouds[_slu][i];
            pItems[_pku].state = ProductState.NotPurchasedYet;
            pItems[_pku].currentOwnerId = msg.sender;
            //pItems[_pku].deistributorId = msg.sender;
            //pItems[_pku].retailerId = _receiver;

        }
        emit Sold(_slu);
} 


    /// Function helps manufacturer to Pack a isManufactured Product Loud
    function purchaseProduct (uint _pku)
        public
        payable
        isProductTaxTracked(_pku)
    {
        pItems[_pku].state = ProductState.Purchased;
        pItems[_pku].currentOwnerId = msg.sender;

        emit Purchased(_pku);
    }
    
    /// public data featching functions
    function fetchProductLoaudData(uint _slu) 
        external 
        view 
        returns(
            uint quantity,
            uint _udpc,
            string memory state,
            address currentOwner,
            address manufacturerId,
            uint price
        )
    {
        require(_slu <= slu && _slu != 0, 'Given SLU Not Created Yet!');

        uint sampleItemPKU = stockLouds[_slu][stockLouds[_slu].length-1];
        (
            _udpc,
            ,
            state,
            currentOwner,
            manufacturerId,
            price,
            ,
            
        ) = fetchProductItemData(sampleItemPKU);

        quantity = stockLouds[_slu].length;
    }

    function fetchProductItemData(uint _pku)
        public
        view
        returns(
            uint _udpc,
            uint _slu,
            string memory state,
            address currentOwner,
            address manufacturerId,
            uint price,
            uint packingTimeStamp,
            uint numberOfTaxUpdate
        )
    {
        require(_pku <= pku && _pku != 0, 'Given PKU Not Created Yet!');
        ProductItem  storage _ProductItem = pItems[_pku];

        _udpc = _ProductItem.udpc;
        _slu = _ProductItem.slu;

        if (_ProductItem.state == ProductState.Manufactured)
            state = 'Manufactured';
        else if (_ProductItem.state == ProductState.Purchased)
            state = 'Purchased';

        currentOwner = _ProductItem.currentOwnerId;
        manufacturerId = _ProductItem.manufacturerId;
        price = _ProductItem.price;
        numberOfTaxUpdate = _ProductItem.taxUpdateCounter;
    }

    function fetchLoudPKUs(uint _slu)
        external
        view
        returns(
            uint[] memory loadPKUs
        )
    {
        loadPKUs = stockLouds[_slu];
    }


    function updateTaxHistory (
        uint _slu,
        uint _paidTax
        //uint _totalTax
    )
        public
    {   
        //uint _totalTax = pItems[_pku].taxHistory[pItems[_pku].taxUpdateCounter-1].totalTax + _paidTax; 
        uint quantity = stockLouds[_slu].length;
        TaxUpdateOpj memory _taxUpdate = TaxUpdateOpj(
            now,
            _paidTax,
            /*_totalTax,*/
            msg.sender
        );
        for (uint i = 0; i < quantity; i++) {
            uint _pku = stockLouds[_slu][i];

            pItems[_pku].taxHistory[pItems[_pku].taxUpdateCounter] = _taxUpdate;
            pItems[_pku].taxUpdateCounter ++;
        }
        emit taxUpdated(_slu);
    }




    function fetchtaxHistory(uint _pku)
        external
        view
        isProductTaxTracked(_pku)
        returns(
            uint numberOfupdate,
            uint[] memory timeStamps,
            uint[] memory lastPaidTax,
           // uint[] memory totalTax,
            address[] memory updaterAddresses
        )
    {
        ProductItem  storage _ProductItem = pItems[_pku];
        numberOfupdate = _ProductItem.taxUpdateCounter;
        uint[] memory _timeStamps = new uint[](numberOfupdate);
        uint[] memory _lastPaidTax = new uint[](numberOfupdate);
       // uint[] memory _totalTax = new uint[](numberOfupdate);
        address[] memory _updaterAddresses = new address[](numberOfupdate);
        for (uint i = 0; i < _ProductItem.taxUpdateCounter; i++) {
            TaxUpdateOpj storage _taxUpdate = _ProductItem.taxHistory[i];
            _timeStamps[i] = _taxUpdate.timeStamp;
            _lastPaidTax[i] = _taxUpdate.lastPaidTax;
            //_totalTax[i] = _taxUpdate.totalTax;
            _updaterAddresses[i] = _taxUpdate.updaterAddress;
        }
        (timeStamps, lastPaidTax, /*totalTax,*/ updaterAddresses) = (
            _timeStamps, 
            _lastPaidTax, 
           // _totalTax,
            _updaterAddresses
        );
    }

}
