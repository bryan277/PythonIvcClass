
#1003181
#CS10 Python Programming Homework 1

#Program Set 3 (10 Points)
#Input
stockName = input('Enter Stock name: ')
numberOfShares = float(input('Enter Number of shares: '))
purchasePrice = float(input('Enter Purchase price: '))
sellingPrice = float(input('Enter selling price: '))
commission = float(input('Enter Commission: '))

#Output
print()
print('Stock Name: ' + stockName)
print()
print('Amount paid for the stock:          $ ' + format(numberOfShares*purchasePrice, ',.2f'))
print('Commission paid on the purchase:    $  ' + format(purchasePrice*commission*10000, ',.2f'))
print('Amount the stock sold for:          $ ' + format(numberOfShares * sellingPrice, ',.2f'))
print('Commision paid on the sale:         $  ' + format(sellingPrice*commission*10000, ',.2f'))
print('Profit (or loss if negative):       $       ' + format((sellingPrice - commission)-(purchasePrice+commission), ',.2f'))


# Enter Stock name: Kaplack,. Inc.
# Enter Number of shares: 10000
# Enter Purchase price: 33.92
# Enter selling price: 35.92
# Enter Commission: 0.04
#
# Stock Name: Kaplack,. Inc.
#
# Amount paid for the stock:          $ 339,200.00
# Commission paid on the purchase:    $  13,568.00
# Amount the stock sold for:          $ 359,200.00
# Commision paid on the sale:         $  14,368.00
# Profit (or loss if negative):       $       1.92
