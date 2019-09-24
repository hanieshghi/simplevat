from django.shortcuts import render
from web3.middleware import geth_poa_middleware
from web3.middleware import pythonic_middleware, attrdict_middleware
from django.http import HttpResponse
from web3 import Web3
import json

# connection definition:===========================================
HTTPUrl = "http://127.0.0.1:7545"
ipc_address = ""
ws = ""

w3 = Web3(Web3.HTTPProvider(HTTPUrl))
#w3.middleware_stack.inject(geth_poa_middleware, layer=0)
#w3.middleware_stack.add(pythonic_middleware)
#w3.middleware_stack.add(attrdict_middleware)
# contract definition:
contract_address = Web3.toChecksumAddress('0x490Ca917914F645DdeD8F8B65709A89d44F92de8')


abi_code = json.loads("""[
    {
      "constant": false,
      "inputs": [],
      "name": "renounceMeFromBuyer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        }
      ],
      "name": "featchProductDesignMetaData",
      "outputs": [
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "description",
          "type": "string"
        },
        {
          "name": "notes",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isManufacturer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "_description",
          "type": "string"
        },
        {
          "name": "_isPassed",
          "type": "bool"
        },
        {
          "name": "_notes",
          "type": "string"
        }
      ],
      "name": "addTestCase",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "recipient",
          "type": "address"
        }
      ],
      "name": "transferPrimary",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        }
      ],
      "name": "approveProduct",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "quantity",
          "type": "uint256"
        }
      ],
      "name": "manufacturProductsLoud",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isBuyer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_pku",
          "type": "uint256"
        }
      ],
      "name": "fetchtaxHistory",
      "outputs": [
        {
          "name": "numberOfupdate",
          "type": "uint256"
        },
        {
          "name": "timeStamps",
          "type": "uint256[]"
        },
        {
          "name": "lastPaidTax",
          "type": "uint256[]"
        },
        {
          "name": "updaterAddresses",
          "type": "address[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "assignMeAsBuyer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "_testIndex",
          "type": "uint256"
        }
      ],
      "name": "featchProductDesignTestCases",
      "outputs": [
        {
          "name": "description",
          "type": "string"
        },
        {
          "name": "isPassed",
          "type": "bool"
        },
        {
          "name": "notes",
          "type": "string"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "_description",
          "type": "string"
        },
        {
          "name": "_isPassed",
          "type": "bool"
        },
        {
          "name": "_notes",
          "type": "string"
        }
      ],
      "name": "addTestCaseByRegulaor",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isPauser",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "assignMeAsManufacturer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        }
      ],
      "name": "purchaseProductDesign",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "paused",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "amIDesigner",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_slu",
          "type": "uint256"
        }
      ],
      "name": "buyProductsLoud",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "renouncePauser",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "_price",
          "type": "uint256"
        }
      ],
      "name": "upForSale",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        }
      ],
      "name": "fetchProductDesignData",
      "outputs": [
        {
          "name": "currentOwner",
          "type": "address"
        },
        {
          "name": "designerId",
          "type": "address"
        },
        {
          "name": "designerName",
          "type": "string"
        },
        {
          "name": "ProductName",
          "type": "string"
        },
        {
          "name": "currentState",
          "type": "string"
        },
        {
          "name": "forSale",
          "type": "bool"
        },
        {
          "name": "salePrice",
          "type": "uint256"
        },
        {
          "name": "numberOfTests",
          "type": "uint256"
        },
        {
          "name": "numberOfManufacturers",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_pku",
          "type": "uint256"
        }
      ],
      "name": "fetchProductItemData",
      "outputs": [
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "_slu",
          "type": "uint256"
        },
        {
          "name": "state",
          "type": "string"
        },
        {
          "name": "currentOwner",
          "type": "address"
        },
        {
          "name": "manufacturerId",
          "type": "address"
        },
        {
          "name": "price",
          "type": "uint256"
        },
        {
          "name": "packingTimeStamp",
          "type": "uint256"
        },
        {
          "name": "numberOfTaxUpdate",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "addPauser",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "isOwner",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "renounceMeFromSeller",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "renounceMeFromManufacturer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "assignMeAsDesigner",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isDesigner",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_slu",
          "type": "uint256"
        },
        {
          "name": "_paidTax",
          "type": "uint256"
        }
      ],
      "name": "updateTaxHistory",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_slu",
          "type": "uint256"
        }
      ],
      "name": "fetchProductLoaudData",
      "outputs": [
        {
          "name": "quantity",
          "type": "uint256"
        },
        {
          "name": "_udpc",
          "type": "uint256"
        },
        {
          "name": "state",
          "type": "string"
        },
        {
          "name": "currentOwner",
          "type": "address"
        },
        {
          "name": "manufacturerId",
          "type": "address"
        },
        {
          "name": "price",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "assignMeAsSeller",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "amISeller",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "taxCollector",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "amIBuyer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "primary",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "_slu",
          "type": "uint256"
        }
      ],
      "name": "fetchLoudPKUs",
      "outputs": [
        {
          "name": "loadPKUs",
          "type": "uint256[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "whoAmI",
      "outputs": [
        {
          "name": "Buyer",
          "type": "bool"
        },
        {
          "name": "Seller",
          "type": "bool"
        },
        {
          "name": "manufacturer",
          "type": "bool"
        },
        {
          "name": "designer",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "amIManufacturer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_designerName",
          "type": "string"
        },
        {
          "name": "_ProductName",
          "type": "string"
        },
        {
          "name": "_description",
          "type": "string"
        },
        {
          "name": "_notes",
          "type": "string"
        }
      ],
      "name": "designProduct",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "renounceMeFromDesigner",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isSeller",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "recipient",
          "type": "address"
        }
      ],
      "name": "PrimaryTransferred",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": true,
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "slu",
          "type": "uint256"
        }
      ],
      "name": "Manufactured",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "slu",
          "type": "uint256"
        }
      ],
      "name": "taxUpdated",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "slu",
          "type": "uint256"
        }
      ],
      "name": "Sold",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "pku",
          "type": "uint256"
        }
      ],
      "name": "Purchased",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "Owned",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "TestCaseAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "Approved",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "UpForSale",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "ProductDesignPurchased",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "udpc",
          "type": "uint256"
        }
      ],
      "name": "SaleCanceled",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Paused",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": false,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "Unpaused",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "PauserAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "PauserRemoved",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "SellerAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "SellerRemoved",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "DesignerAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "DesignerRemoved",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "ManufacturerAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "ManufacturerRemoved",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "BuyerAdded",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "name": "account",
          "type": "address"
        }
      ],
      "name": "BuyerRemoved",
      "type": "event"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "kill",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_pku",
          "type": "uint256"
        }
      ],
      "name": "purchaseProduct",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function"
    }
  ]""")

print(w3.isConnected())

supply_contract = w3.eth.contract(address=contract_address, abi=abi_code)

# set default account:
w3.eth.defaultAccount = w3.eth.accounts[6]
#default account is w3.eth.accounts[0], you can change 0 to 1 to 14 for tests.
#all accounts are unlocked.
default_account = w3.eth.defaultAccount


def currentAccountRoles():
    myRoles = supply_contract.functions.whoAmI().call()
    return myRoles


def assignMeAsDesigner():
    tx = supply_contract.functions.assignMeAsDesigner().transact()
    return tx



def assignMeAsManufacturer():
    tx = supply_contract.functions.assignMeAsManufacturer().transact()
    return tx



def assignMeAsBuyer():
    tx = supply_contract.functions.assignMeAsBuyer().transact()
    return tx


def renounceMeFromDesigner():
    tx = supply_contract.functions.renounceMeFromDesigner().transact()
    return tx


def renounceMeFromManufacturer():
    tx = supply_contract.functions.renounceMeFromManufacturer().transact()
    return tx


def renounceMeFromBuyer():
    tx = supply_contract.functions.renounceMeFromBuyer().transact()
    return tx


def designProduct(_designerName, _ProductName, _description, _notes):
    tx = supply_contract.functions.designProduct(str(_designerName), str(
        _ProductName), str(_designerName), str(_notes)).transact()
    return tx



def approveProduct(_udpc):
    tx = supply_contract.functions.approveProduct(int(_udpc)).transact()
    return tx


def upForSale(_udpc, _price):
    price_in_ether = int(_price)  # later use util to change _price to WEI.
    tx = supply_contract.functions.upForSale(int(_udpc),price_in_ether).transact()
    return tx


def purchaseProductDesign(_udpc, _price):
    price_in_ether = int(_price)  # later use util to change _price into WEI
    tx = supply_contract.functions.purchaseProductDesign(
        int(_udpc)).transact({'value': price_in_ether})
    return tx

def manufacturProductsLoud(_udpc, quantity):
    tx = supply_contract.functions.manufacturProductsLoud(
        int(_udpc), int(quantity)).transact()
    return tx


def addProductsLoud(_slu, _unitPrice):
    price_in_ether = int(_unitPrice)  # later use util to convert it to WEI
    tx = supply_contract.functions.addProductsLoud(
        int(_slu), price_in_ether).transact()
    return tx


def buyProductsLoud(_slu, _receiver, _price):
    price_in_ether = int(_price)  # later use util to convert it to WEI
    tx = supply_contract.functions.buyProductsLoud(
        int(_slu), Web3.toChecksumAddress(_receiver)).transact({'value': price_in_ether})
    return tx

def updateTaxHistory(_slu, lastPaidTax):
    tx = supply_contract.functions.updateTaxHistory(
        int(_slu), int(lastPaidTax)).transact()
    return tx


def purchaseProduct(_pku, _price):
    price_in_ether = int(_price)
    tx = supply_contract.functions.purchaseProduct(
        int(_pku)).transact({'value': price_in_ether})
    return tx


def fetchProductDesignData(_udpc):
    Product_design_data = supply_contract.functions.fetchProductDesignData(
        int(_udpc)).call()
    return Product_design_data


def fetchProductLoaudData(_slu):
    Product_load_data = supply_contract.functions.fetchProductLoaudData(
        int(_slu)).call()
    return Product_load_data


def fetchLoudPKUs(_slu):
    Product_loadPKUs = supply_contract.functions.fetchLoudPKUs(int(_slu)).call()
    return Product_loadPKUs


def fetchProductItemData(_pku):
    Product_data = supply_contract.functions.fetchProductItemData(int(_pku)).call()
    return Product_data


def fetchTaxHistory(_pku):
    Product_env_history = supply_contract.functions.fetchTaxHistory(
        int(_pku)).call()
    return Product_env_history


# =================================================================

# Create your views here.


def home(request):
    if (request.POST.get('isAjax') == 'true'):
        response_data = {}
        if(request.POST.get('func') == 'currentAccountRoles'):
            response_data['res_data'] = currentAccountRoles()
            return HttpResponse(json.dumps(response_data), content_type="application/json")


        elif(request.POST.get('func') == 'assignMeAsBuyer'):
            try:
                response_data['res_data'] = assignMeAsBuyer().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'renounceMeFromBuyer'):
            try:
                response_data['res_data'] = renounceMeFromBuyer().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'assignMeAsManufacturer'):
            try:
                response_data['res_data'] = assignMeAsManufacturer().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'renounceMeFromManufacturer'):
            try:
                response_data['res_data'] = renounceMeFromManufacturer().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            
        elif(request.POST.get('func') == 'assignMeAsDesigner'):
            try:
                response_data['res_data'] = assignMeAsDesigner().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'renounceMeFromDesigner'):
            try:
                response_data['res_data'] = renounceMeFromDesigner().hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'designProduct'):
            try:
                response_data['res_data'] = designProduct(request.POST.get('designerName'), request.POST.get('ProductName'), request.POST.get('describtion'), request.POST.get('note')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'approveProduct'):
            try:
                response_data['res_data'] = approveProduct(request.POST.get('udpc')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'upForSale'):
            try:
                response_data['res_data'] = upForSale(request.POST.get('udpc'), request.POST.get('price')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'purchaseProductDesign'):
            try:
                response_data['res_data'] = purchaseProductDesign(request.POST.get('udpc'), request.POST.get('price')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'manufacturProductsLoud'):
            try:
                response_data['res_data'] = manufacturProductsLoud(request.POST.get('udpc'), request.POST.get('quantity')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")


        elif(request.POST.get('func') == 'addProductsLoud'):
            try:
                response_data['res_data'] = addProductsLoud(request.POST.get('slu'), request.POST.get('unit_price')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'buyProductsLoud'):
            try:
                response_data['res_data'] = buyProductsLoud(request.POST.get('slu'), request.POST.get('retailer_address'), request.POST.get('ether_value')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'updateTaxHistory'):
            try:
                response_data['res_data'] = updateTaxHistory(request.POST.get('slu'), request.POST.get('lastPaidTax')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")


        elif(request.POST.get('func') == 'purchaseProduct'):
            try:
                response_data['res_data'] = purchaseProduct(request.POST.get('pku'), request.POST.get('ether_value')).hex()
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'fetchProductDesignData'):
            try:
                response_data['res_data'] = fetchProductDesignData(request.POST.get('udpc'))
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'fetchProductLoaudData'):
            try:
                response_data['res_data'] = fetchProductLoaudData(request.POST.get('slu'))
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")
                
        elif(request.POST.get('func') == 'fetchLoudPKUs'):
            try:
                response_data['res_data'] = fetchLoudPKUs(request.POST.get('slu'))
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif(request.POST.get('func') == 'fetchProductItemData'):
            try:
                response_data['res_data'] = fetchProductItemData(request.POST.get('pku'))
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        elif(request.POST.get('func') == 'fetchTaxHistory'):
            try:
                response_data['res_data'] = fetchTaxHistory(
                    request.POST.get('pku'))
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            except Exception as e:
                response_data['res_data'] = str(e)
                return HttpResponse(json.dumps(response_data), content_type="application/json")

    return render(request, 'home.html', {'conn': w3.eth.defaultAccount, 'network': HTTPUrl})