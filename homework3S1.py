
#CS 10
#1003181
#Due on Exam 3
#Homework 3 set 1


# 1. Write a function(s) to allow the user to input the followings:

def input1()->(str, float, float, float, float):
    nameStock = input('Enter stock name : ')
    numberOfShares = float(input('Enter Number of shares: '))
    purchasePrice = float(input('Enter Purchase price: '))
    sellingPrice = float(input('Enter selling price: '))
    commission = float(input('Enter Commission: '))
    return nameStock, numberOfShares, purchasePrice, sellingPrice, commission

def calculate(numberOfShares: float, purchasePrice: float, sellingPrice: float, commission: float)->(float, float, float, float, float):
    paidStocks = numberOfShares*purchasePrice
    commission1 = purchasePrice*commission*10000
    stockSold = numberOfShares * sellingPrice
    commBroker = sellingPrice*commission*10000
    profitLoss = (sellingPrice - commission)-(purchasePrice+commission)
    return paidStocks, commission1, stockSold, commBroker, profitLoss
# TypeError: calculate() missing 4 required positional arguments: 'numberOfShares', 'purchasePrice', 'sellingPrice', and 'commission'


def output(nameStock:str, paidStocks: float, commission1: float, stockSold: float, commBroker: float, profitLoss: float):
    print('Stock Name: ' + stockName)
    print()
    print('Amount paid for the stock:          $ ' + format(paidStocks, ',.2f'))
    print('Commission paid on the purchase:    $  ' + format(commission, ',.2f'))
    print('Amount the stock sold for:          $ ' + format(stockSold, ',.2f'))
    print('Commision paid on the sale:         $  ' + format(commBroker, ',.2f'))
    print('Profit (or loss if negative):       $       ' + format(profiLoss , ',.2f'))

def main():
    input1()
    calculate()
    output()

if __name__=="__main__":
    main()
