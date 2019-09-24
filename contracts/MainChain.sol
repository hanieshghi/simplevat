pragma solidity ^0.5.0;

/// Import supply chain `Base` contract
import "./SupplyChain.sol";

/// Import `Ownable` contract from OpenZeppelin package
import "./openzeppelin/contracts/ownership/Ownable.sol";

/// Import `Secondary` contract from OpenZeppelin package
import "./openzeppelin/contracts/ownership/Secondary.sol";

/// @title Main Chain Contract 
/// @dev  **TODO** this contract will use Proxy to make the suply chain upgradable
contract MainChain is SupplyChain, Ownable, Secondary {
    constructor() public {

    }

    // Kill function if required
    function kill() public onlyOwner() {
        selfdestruct(msg.sender);
    }

    function purchaseProduct (uint _pku)
        public
        payable
    {
        super.purchaseProduct(_pku);

        uint price = pItems[_pku].price;
        address payable developerId = address(uint160(owner()));
        uint developerBounty = price*1 /100;
        developerId.transfer(developerBounty);

    }

}
