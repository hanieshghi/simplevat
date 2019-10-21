from django.shortcuts import render,redirect
from django.core.paginator import Paginator
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
      "constant": false,
      "inputs": [
        {
          "name": "_pID",
          "type": "uint256"
        }
      ],
      "name": "setCustomerRecieved",
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
        },
        {
          "name": "customerRecieved",
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
      "name": "getLastPID",
      "outputs": [
        {
          "name": "",
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
          "name": "_pID",
          "type": "uint256"
        }
      ],
      "name": "getCustomerRecieved",
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
w3.eth.defaultAccount = w3.eth.accounts[6]
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
    #print('price' ,_price)
    
    totalprice = _price + _price * 9/100
    # print('totalprice' ,totalprice)
    # print('INTtotalprice' ,int(totalprice))
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
    #newPrice = w3.toWei(newPrice , 'ether')
    tx = supply_contract.functions.setNewPrice(
        int(pID) , int(newPrice)).transact()
    return tx

def setCustomerRecieved(pID):
    tx = supply_contract.functions.setCustomerRecieved(
        int(pID)).transact()
    return tx

def getCustomerRecieved(pID):
    customerRecieved = supply_contract.functions.getCustomerRecieved(
        int(pID)).call()
    return customerRecieved

def getLatestPID():
    lastPID = supply_contract.functions.getLastPID().call()
    return lastPID
# =================================================================

# Create your views here.
def purchase(request):

    pdata=last_6_Products(request)
    txData = getTransactions(request)

    print("asflkjasd;jflkajsdf")
    newPriceFlag = True
    if request.method == 'POST':
        priceChanged = False
        pID = request.POST['pID']
        customerRecieved = getCustomerRecieved(pID)
        print("asflkjasd;jflkajsdf",customerRecieved)
        if customerRecieved:
            return render(request, 'home.html' , {'txData':txData,'data':pdata,'error':'This Product Can not be purchased!'})

        data = fetchProductItemData(pID)
        price = data[4]

        if 'newPrice' in request.POST:
            newPrice = int(request.POST['newPrice'])
            newPrice = w3.toWei(newPrice , 'ether')
            if newPrice < price :
                return render(request, 'home.html' , {'txData':txData,'data':pdata,'error':'new Price must be bigger!'})
            priceChanged = True
        
        if not customerRecieved:
            tx = purchaseProduct(pID, price)
            
        
        if priceChanged:
            setNewPrice(pID , newPrice )
        elif not priceChanged:
            setCustomerRecieved(pID)
        newPriceFlag = False  
        pdata=last_6_Products(request)
        txData = getTransactions(request)
        return render(request, 'home.html' , {'txData':txData,'data':pdata,'msg':'Purchase was Successfull!','newPriceFlag':newPriceFlag})
   
def last_6_Products(request):
    data = allProducts(request)
    return data[:6]

def getProducts(request, product_id):
    if request.method == 'POST':
        if request.POST['pID']:
            product_id = int(request.POST['pID'])
            return redirect('/product/'+ str(product_id))
         
    if request.method == 'GET':
        data = fetchProductItemData(product_id)
        name = data[1]
        currentOwner = data[2]
        manufacturerId = data[3]
        price = data[4]/10**18
        totalPaidTax = data[5]/10**18
        lastPaidTax = data[6]/10**18
        numberOfTaxUpdate = data[7]
        customerRecieved = data[8]
        return render(request, 'getProducts.html', {'pID': product_id , 'name':name ,
            'currentOwner':currentOwner , 'manufacturerId': manufacturerId , 'price':price,
            'totalPaidTax': totalPaidTax , 'lastPaidTax':lastPaidTax , 'numberOfTaxUpdate':numberOfTaxUpdate,'customerRecieved':customerRecieved})
    else:
      return render(request, 'home.html' ,{'error':'Enter ID!'})

def generateProduct(request):
    if request.method == 'POST':
      if request.POST['name'] and request.POST['price'] and request.POST['taxPaid']:

        name = request.POST['name']
        price = request.POST['price']
        weiPrice = Web3.toWei(price, 'ether')
        tax = request.POST['taxPaid']
        weiTax = Web3.toWei(tax, 'ether')
        manufacturProductsLouds(weiPrice, weiTax, name)
        pID = getLatestPID()
        print(pID)
        return redirect('/product/'+ str(pID)) # '/products/'+ str(product.id))
        
      else:
        return render(request , 'generateProduct.html', {'error':'all fields must be filled!'})
    else:  
      return render(request, 'generateProduct.html' )

def allProducts(request):
    alldata=[]
    latest = getLatestPID()
    for pID in range(1,latest+1):
        sendingData =[]
        data = fetchProductItemData(pID)
        sendingData.append(pID)
        name = data[1]
        sendingData.append(name)
        currentOwner = data[2]
        sendingData.append(currentOwner)
        manufacturerId = data[3]
        sendingData.append(manufacturerId)
        price = data[4]/10**18
        sendingData.append(price)
        totalPaidTax = data[5]/10**18
        sendingData.append(totalPaidTax)
        lastPaidTax = data[6]/10**18
        sendingData.append(lastPaidTax)
        numberOfTaxUpdate = data[7]
        sendingData.append(numberOfTaxUpdate)
        customerRecieved = data[8]
        sendingData.append(customerRecieved)

        alldata.append(sendingData)
    alldata = sorted(alldata , reverse=True)
    return alldata

def products(request):
    allproducts = allProducts(request)
    paginator = Paginator(allproducts, 9) # Show 12 contacts per page

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'products.html', {'data': products})

def taxhistory(request ,product_id ):
    if request.method == 'POST':
        if request.POST['pID']:
            product_id = int(request.POST['pID'])
            return redirect('/taxhistory/'+ str(product_id))

    if request.method == 'GET':
        taxdata = fetchTaxHistory(product_id)
        numberOfupdate = taxdata[0]
        timeStamps = [datetime.fromtimestamp(i).isoformat() for i in taxdata[1]]
        lastPaidTax = [i/10**18 for i in taxdata[2]]
        totalTax = taxdata[3][-1]/10**18
        updaterAddresses = taxdata[4]
        return render(request, 'taxhistory.html', {'pID': product_id , 'numberOfupdate':numberOfupdate ,
        'timeStamps':timeStamps , 'lastPaidTax': lastPaidTax , 'totalTax':totalTax,
        'updaterAddresses': updaterAddresses })
    else:
        return render(request, 'home.html' ,{'error':'Enter ID!'})

def getTransactions(request):
    mylist = []
    allTX=[]
    blockNumber = w3.eth.blockNumber
    txcount = w3.eth.getBlockTransactionCount(blockNumber)


    data = w3.eth.getBlock(blockNumber)
    txdata = w3.eth.getTransactionByBlock(blockNumber, 0)
    
    txhash = w3.toHex(txdata['hash'])[:40]
    txfrom = txdata['from']
    txto = txdata['to']
    #txvalue = txdata['value']
    mylist = [txhash,txfrom, txto]
    print(txdata)
    allTX.append(mylist)
    return allTX

def home(request):
    #request.POST.get('input')
    data=last_6_Products(request)
    txData = getTransactions(request)
    if request.method == 'POST':
        if "view" in request.POST:
            return (getProducts(request ,request.POST['pID'] ))

        elif "taxhistory" in request.POST:
            return (taxhistory(request ,request.POST['pID'] ))
        
        elif "purchase" in request.POST:
            if '1' in request.POST.getlist('customer') or 'newPrice' in request.POST:
                return (purchase(request ))
            else:
                return render(request, 'home.html' ,{'data':data,'txData':txData,'error':'Enter new Price!','newPriceFlag':True})

    else:
        
        return render(request, 'home.html', {'txData':txData,'data':data,'conn': w3.eth.defaultAccount, 'network': HTTPUrl})
