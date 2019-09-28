from django.shortcuts import render
from web3.middleware import geth_poa_middleware
from web3.middleware import pythonic_middleware, attrdict_middleware
from django.http import HttpResponse
from web3 import Web3
from datetime import datetime
import json

# connection definition:===========================================
HTTPUrl = "http://127.0.0.1:7545"
ipc_address = ""
ws = ""

w3 = Web3(Web3.HTTPProvider(HTTPUrl))
#w3.middleware_stack.inject(geth_poa_middleware, layer=0)
# w3.middleware_stack.add(pythonic_middleware)
# w3.middleware_stack.add(attrdict_middleware)
# contract definition:
contract_address = Web3.toChecksumAddress(
    '0x490Ca917914F645DdeD8F8B65709A89d44F92de8')

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
          "name": "_pID",
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
          "name": "totalTax",
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
      "inputs": [
        {
          "name": "_pID",
          "type": "uint256"
        }
      ],
      "name": "purchaseProduct",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
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
      "constant": true,
      "inputs": [
        {
          "name": "_pID",
          "type": "uint256"
        }
      ],
      "name": "fetchProductItemData",
      "outputs": [
        {
          "name": "pID",
          "type": "uint256"
        },
        {
          "name": "name",
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
          "name": "totalTax",
          "type": "uint256"
        },
        {
          "name": "lastPaidTax",
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
      "name": "renounceMeFromManufacturer",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [
        {
          "name": "_pID",
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
      "constant": false,
      "inputs": [
        {
          "name": "_price",
          "type": "uint256"
        },
        {
          "name": "_tax",
          "type": "uint256"
        },
        {
          "name": "_name",
          "type": "string"
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
      "inputs": [],
      "name": "whoAmI",
      "outputs": [
        {
          "name": "Buyer",
          "type": "bool"
        },
        {
          "name": "manufacturer",
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
          "name": "_pID",
          "type": "uint256"
        },
        {
          "name": "newPrice",
          "type": "uint256"
        }
      ],
      "name": "setNewPrice",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
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
          "name": "pID",
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
          "name": "pID",
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
          "name": "pID",
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
    }
  ]""")

print(w3.isConnected())

supply_contract = w3.eth.contract(address=contract_address, abi=abi_code)

# set default account:
w3.eth.defaultAccount = w3.eth.accounts[3]
# default account is w3.eth.accounts[0], you can change 0 to 1 to 14 for tests.
# all accounts are unlocked.
default_account = w3.eth.defaultAccount

 
# supply_contract = w3.eth.contract(abi=abi_code, bytecode=bytecode)
# tx_hash = supply_contract.constructor().transact()
# tx_receipt = w3.eth.waitforTransactionReceipt(tx_hash)
# supply_contract = w3.eth.contract(address= tx_receipt.contract_address , abi = abi_code)

# print(supply_contract.functions.manufacturProductsLoud(10, 1, "test"))
# print(supply_contract.functions.fetchProductItemData(1) )

#testlist = supply_contract.functions.fetchProductItemData(1).pID
# print(testlist)


def currentAccountRoles():
    myRoles = supply_contract.functions.whoAmI().call()
    return myRoles


def assignMeAsManufacturer():
    tx = supply_contract.functions.assignMeAsManufacturer().transact()
    return tx


def assignMeAsBuyer():
    tx = supply_contract.functions.assignMeAsBuyer().transact()
    return tx


def renounceMeFromManufacturer():
    tx = supply_contract.functions.renounceMeFromManufacturer().transact()
    return tx


def renounceMeFromBuyer():
    tx = supply_contract.functions.renounceMeFromBuyer().transact()
    return tx


def manufacturProductsLouds(_price, _tax, _name):
    tx = supply_contract.functions.manufacturProductsLoud(
        int(_price), int(_tax), str(_name)).transact()
    return tx


def updateTaxHistory(_slu, lastPaidTax):
    tx = supply_contract.functions.updateTaxHistory(
        int(_slu), int(lastPaidTax)).transact()
    return tx


def purchaseProduct(_pku, _price):
    
    #price_in_wei = w3.toWei(_price, 'ether')
    print('price' ,_price)
    
    totalprice = _price + _price * 9/100
    print('totalprice' ,totalprice)
    print('INTtotalprice' ,int(totalprice))
    #totalprice = w3.fromWei(totalprice_wei,'ether')
    tx = supply_contract.functions.purchaseProduct(
        int(_pku)).transact({'value':  int(totalprice)})
    return tx


def fetchProductItemData(_pku):
    Product_data = supply_contract.functions.fetchProductItemData(
        int(_pku)).call()
    return Product_data


def fetchTaxHistory(_pku):
    Product_env_history = supply_contract.functions.fetchtaxHistory(
        int(_pku)).call()
    return Product_env_history

def setNewPrice(pID , newPrice):
    newPrice = w3.toWei(newPrice , 'ether')
    tx = supply_contract.functions.setNewPrice(
        int(pID) , int(newPrice)).transact()
    
    return tx

# =================================================================

# Create your views here.
def purchase(request):
    pID = request.GET['pID']
    data = fetchProductItemData(pID)
    price = data[4]
    purchaseProduct(pID, price)
    return render(request, 'purchase.html' , {'pID':pID})

def getNewPrice(request):
    newPrice = request.GET['newPrice']
    pID = request.GET['pID']
    setNewPrice(pID , newPrice )
    return render(request, 'newPrice.html')

def getProducts(request):
    pID = request.GET['pID']
    data = fetchProductItemData(pID)
    name = data[1]
    currentOwner = data[2]
    manufacturerId = data[3]
    price = data[4]/10**18
    totalPaidTax = data[5]/10**18
    lastPaidTax = data[6]/10**18
    numberOfTaxUpdate = data[7]

    return render(request, 'getProducts.html', {'pID': pID , 'name':name ,
    'currentOwner':currentOwner , 'manufacturerId': manufacturerId , 'price':price,
    'totalPaidTax': totalPaidTax , 'lastPaidTax':lastPaidTax , 'numberOfTaxUpdate':numberOfTaxUpdate})


def generateProduct(request):
    
    return render(request, 'generateProduct.html' )


def submitproduct(request):
    name = request.GET['name']
    price = request.GET['price']
    weiPrice = Web3.toWei(price, 'ether')
    tax = request.GET['taxPaid']
    weiTax = Web3.toWei(tax, 'ether')

    # assignMeAsManufacturer()
    manufacturProductsLouds(weiPrice, weiTax, name)
    #manufacturProductsLouds(2, 2, "Name")

    return render(request, 'submitproduct.html')

def taxhistory(request):
    pID = request.GET['pID']
    taxdata = fetchTaxHistory(pID)

    numberOfupdate = taxdata[0]
    timeStamps = [datetime.fromtimestamp(i).isoformat() for i in taxdata[1]]
    lastPaidTax = [i/10**18 for i in taxdata[2]]
    totalTax = taxdata[3][-1]/10**18
    updaterAddresses = taxdata[4]

    return render(request, 'taxhistory.html', {'pID': pID , 'numberOfupdate':numberOfupdate ,
    'timeStamps':timeStamps , 'lastPaidTax': lastPaidTax , 'totalTax':totalTax,
    'updaterAddresses': updaterAddresses })

def home(request):
    request.POST.get('input')
    return render(request, 'home.html', {'conn': w3.eth.defaultAccount, 'network': HTTPUrl})
