pragma solidity ^0.5.0;

/// Import Partnerships library
//import "./Partnerships.sol";

contract ProductDesign {

    /// Variable for tracking Universal Product Product Code (UDPC)
    uint udpc;

    /// Public mapping from UDPC to a Product Design Item
    mapping (uint => ProductDesignItem) pDItems;

    /// Enumaration for defining variety of Product Design State
    enum ProductDesignState {
        Owned,
        Tested,
        Approved,
        ForSale
    }

    /// Structure keeping meta data for a Product Design **TODO**
    struct ProductDesignMeta {
        string name;
        string description;
        string notes;
    }

    /// Structure for Product Design Test Case **TODO**
    struct ProductDesignTestCase {
        address testerId;
        uint timeStamp;
        bool isPassed;
        string description;
        string notes;
    }

    /// Structure for keeping Product Design fields structured
    struct ProductDesignItem {
        uint udpc;
        address payable currentOwner;
        address designerId;
        string designerName;
        ProductDesignState state;
        ProductDesignMeta metaData;
        uint salePrice;
        uint testIndexed;
        mapping(uint => ProductDesignTestCase) testCases;
        //Partnerships.Partnership manufacturers;
    }

    /// Event to emit them for users in functions, accept `udpc` as input
    event Owned(uint udpc);
    event TestCaseAdded(uint udpc);
    event Approved(uint udpc);
    event UpForSale(uint udpc);
    event ProductDesignPurchased(uint udpc);
    event SaleCanceled(uint udpc);

    /// Modifier that checks the paid enough as expected and refunds the remaining balance
    modifier checkProductDesignPaymentValue(uint _udpc) {
        require(msg.value >= pDItems[_udpc].salePrice, "Not Enough!");
        _;
        uint _price = pDItems[_udpc].salePrice;
        uint amountToReturn = msg.value - _price;
        if (amountToReturn != 0)
            address(msg.sender).transfer(amountToReturn);
    }

    /// Modifier that checks if an ProductDesignItem.state of a udpc is Owned
    modifier isOwned(uint _udpc) {
        require(pDItems[_udpc].state == ProductDesignState.Owned);
        _;
    }


    /// Modifier that checks if the caller he is the currentOwner of Product Design
    modifier onlyOwnerOf(uint _udpc) {
        require(pDItems[_udpc].currentOwner == msg.sender);
        _;
    }


    /// Constructor Function sets up UDPC to 0
    constructor() public {
        udpc = 0;
    }

    /// Function helps Designer to estaplish a new Product Design
    function designProduct(
        string memory _designerName,
        string memory _ProductName,
        string memory _description,
        string memory _notes
    )
        public
    {
        udpc ++;
        ProductDesignItem memory newDDItem;
        newDDItem.udpc = udpc;
        newDDItem.currentOwner = msg.sender;
        newDDItem.designerId = msg.sender;
        newDDItem.designerName = _designerName;
        newDDItem.state = ProductDesignState.Owned;
        newDDItem.metaData = ProductDesignMeta(_ProductName, _description, _notes);
        newDDItem.salePrice = 0;
        pDItems[udpc] = newDDItem;
        emit Owned(udpc);
    }

    /// Add Test Case for Product Design by currentOwner
    function addTestCase(
        uint _udpc,
        string memory _description,
        bool _isPassed,
        string memory _notes
    )
        public
        // onlyOwnerOf(_udpc) ==>uncomment this after test
    {
        require(_udpc <= udpc, 'Given UDPC Not Created Yet!');
        ProductDesignTestCase memory _ddtc = ProductDesignTestCase(
            msg.sender,
            block.timestamp,
            _isPassed,
            _description,
            _notes
        );
        pDItems[_udpc].testCases[pDItems[_udpc].testIndexed] = _ddtc;
        pDItems[_udpc].testIndexed ++;
        if (pDItems[_udpc].state == ProductDesignState.Owned)
            pDItems[_udpc].state = ProductDesignState.Tested;
        emit TestCaseAdded(_udpc);
    }

    // Add Test Case for Product Design by regulator
    function addTestCaseByRegulaor(
        uint _udpc,
        string memory _description,
        bool _isPassed,
        string memory _notes
    )
        public
    {
        require(_udpc <= udpc, 'Given UDPC Not Created Yet!');
        ProductDesignTestCase memory _ddtc = ProductDesignTestCase(
            msg.sender,
            block.timestamp,
            _isPassed,
            _description,
            _notes
        );
        pDItems[_udpc].testCases[pDItems[_udpc].testIndexed] = _ddtc;
        pDItems[_udpc].testIndexed ++;
        if (pDItems[_udpc].state == ProductDesignState.Owned)
            pDItems[_udpc].state = ProductDesignState.Tested;

        emit TestCaseAdded(_udpc);
    }

    /// Function to approve Product by a regulator only
    function approveProduct(uint _udpc) public isTested(_udpc) {
        pDItems[_udpc].state = ProductDesignState.Approved;

        emit Approved(_udpc);
    }

    /// Function to sale a Product design
    function upForSale(uint _udpc,uint _price)
        public
        onlyOwnerOf(_udpc)
        isApproved(_udpc)
    {
        pDItems[_udpc].salePrice = _price;
        pDItems[_udpc].state = ProductDesignState.ForSale;

        emit UpForSale(_udpc);
    }


    function fetchProductDesignData(uint _udpc) 
        external 
        view 
        returns(
            address currentOwner,
            address designerId,
            string memory designerName,
            string memory ProductName,
            string memory currentState,
            bool forSale,
            uint salePrice,
            uint numberOfTests,
            uint numberOfManufacturers
        )
    {
        require(_udpc <= udpc, 'Given UDPC Not Created Yet!');
        currentOwner = pDItems[_udpc].currentOwner;
        designerId = pDItems[_udpc].designerId;
        designerName = pDItems[_udpc].designerName;
        ProductName = pDItems[_udpc].metaData.name;

        if (pDItems[_udpc].state == ProductDesignState.Owned)
            currentState = 'Created';
        else if (pDItems[_udpc].state == ProductDesignState.Tested)
            currentState = 'Tested';
        else if (pDItems[_udpc].state == ProductDesignState.Approved)
            currentState = 'Approved';
        else if (pDItems[_udpc].state == ProductDesignState.ForSale)
            currentState = 'ForSale';
        else if (pDItems[_udpc].state == ProductDesignState.ForSale)
            currentState = 'ForSale';

        forSale = (pDItems[_udpc].salePrice != 0);
        salePrice = pDItems[_udpc].salePrice;

        numberOfTests = pDItems[_udpc].testIndexed;
    }

    function featchProductDesignMetaData(uint _udpc) 
        external
        view
        returns(
            string memory name,
            string memory description,
            string memory notes
        )
    {
        require(_udpc <= udpc, 'Given UDPC Not Created Yet!');
        (name, description, notes) = (
            pDItems[_udpc].metaData.name,
            pDItems[_udpc].metaData.description,
            pDItems[_udpc].metaData.notes
        );
    }


}
