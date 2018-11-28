
#1003181
#CS Python Programming Homework 2 Set 3

#Input from user
timesStocks = int(input('How many stocks do you want to enter?: '))

#for loop. if user inputs 6, it will run to through loop 6 times.
for number in range(timesStocks): #range(6)
    stockName = input('Enter Stock name: ')
    numberOfShares = float(input('Enter Number of shares: '))
    purchasePrice = float(input('Enter Purchase price: '))
    sellingPrice = float(input('Enter selling price: '))
    commission = float(input('Enter Commission: '))


    print()
    print('Stock Name: ' + stockName)
    print()
    print('Amount paid for the stock:          $ ' + format(numberOfShares32*purchasePrice, ',.2f'))
    print('Commission paid on the purchase:    $  ' + format(purchasePrice*commission*10000, ',.2f'))
    print('Amount the stock sold for:          $ ' + format(numberOfShares * sellingPrice, ',.2f'))
    print('Commision paid on the sale:         $  ' + format(sellingPrice*commission*10000, ',.2f'))
    print('Profit (or loss if negative):       $       ' + format((sellingPrice - commission)-(purchasePrice+commission), ',.2f'))

#Output
# How many stocks do you want to enter?: 3
# Enter Stock name: Apple, Inc.
# Enter Number of shares: 10000
# Enter Purchase price: 35.92
# Enter selling price: 32.92
# Enter Commission: 0.04
#
# Stock Name: Apple, Inc.
#
# Amount paid for the stock:          $ 359,200.00
# Commission paid on the purchase:    $  14,368.00
# Amount the stock sold for:          $ 329,200.00
# Commision paid on the sale:         $  13,168.00
# Profit (or loss if negative):       $      -3.08
# Enter Stock name: Kaplan, Inc.
# Enter Number of shares: 10000
# Enter Purchase price: 32.92
# Enter selling price: 33.92
# Enter Commission: 0.04
#
# Stock Name: Kaplan, Inc.
#
# Amount paid for the stock:          $ 329,200.00
# Commission paid on the purchase:    $  13,168.00
# Amount the stock sold for:          $ 339,200.00
# Commision paid on the sale:         $  13,568.00
# Profit (or loss if negative):       $       0.92
# Enter Stock name: Google
# Enter Number of shares: 10000
# Enter Purchase price: 43.33
# Enter selling price: 45.22
# Enter Commission: 0.04
#
# Stock Name: Google
#
# Amount paid for the stock:          $ 433,300.00
# Commission paid on the purchase:    $  17,332.00
# Amount the stock sold for:          $ 452,200.00
# Commision paid on the sale:         $  18,088.00
# Profit (or loss if negative):       $       1.81
