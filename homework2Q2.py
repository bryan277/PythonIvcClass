
#1003181
#CS Python Programming Homework 2 Set 2

#Input
stockName = input('Enter Stock name or type "Quit" to quit program: ')

#while loop, if user inputs quit, it will end the program
while stockName != 'Quit' and stockName != 'quit':
    numberOfShares = float(input('Enter Number of shares: '))
    purchasePrice = float(input('Enter Purchase price: '))
    sellingPrice = float(input('Enter selling price: '))
    commission = float(input('Enter Commission: '))
    print()
    print('Stock Name: ' + stockName)
    print()
    print('Amount paid for the stock:          $ ' + format(numberOfShares*purchasePrice, ',.2f'))
    print('Commission paid on the purchase:    $  ' + format(purchasePrice*commission*10000, ',.2f'))
    print('Amount the stock sold for:          $ ' + format(numberOfShares * sellingPrice, ',.2f'))
    print('Commision paid on the sale:         $  ' + format(sellingPrice*commission*10000, ',.2f'))
    print('Profit (or loss if negative):       $       ' + format((sellingPrice - commission)-(purchasePrice+commission), ',.2f'))
    print()
    stockName = input('Enter New Stock name or type "Quit" to quit program: ')

#Output
# Enter Stock name or type "Quit" to quit program: Schmoe, Inc.
# Enter Number of shares: 10000
# Enter Purchase price: 33.92
# Enter selling price: 35.92
# Enter Commission: 0.04
#
# Stock Name: Schmoe, Inc.
#
# Amount paid for the stock:          $ 339,200.00
# Commission paid on the purchase:    $  13,568.00
# Amount the stock sold for:          $ 359,200.00
# Commision paid on the sale:         $  14,368.00
# Profit (or loss if negative):       $       1.92
#
# Enter New Stock name or type "Quit" to quit program: Kaplack,. Inc.
# Enter Number of shares: 10000
# Enter Purchase price: 30.54
# Enter selling price: 32.33
# Enter Commission: 0.04
#
# Stock Name: Kaplack,. Inc.
#
# Amount paid for the stock:          $ 305,400.00
# Commission paid on the purchase:    $  12,216.00
# Amount the stock sold for:          $ 323,300.00
# Commision paid on the sale:         $  12,932.00
# Profit (or loss if negative):       $       1.71
#
# Enter New Stock name or type "Quit" to quit program: Quit
