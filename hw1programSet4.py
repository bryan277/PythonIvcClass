
#1003181
#CS10 Python Programming Homework 1

#Program Set 4 (10 points)
#input
quantity = float(input('Enter the quantity of item sold: '))
value = float(input('Enter the value of item : '))
discount = float(input('Enter the discount percentage: '))
tax = float(input('Enter the tax: '))

#formulas
amount = quantity * value
discountAmount = amount * discount/100
subTotal = amount - discountAmount
taxAmount = subTotal * tax/100
totalAmount = subTotal + taxAmount

#output
print()
print('*********BILL*********')
print('Quantity sold: ', format(quantity, '18.2f'))
print('Price per item: ', format(value, '17.2f'))
print()
print('                         _________')
print('Amount:                  ', format(amount, ',.2f'))
print('Discount:               -', format(discountAmount, '8.2f'))
print('                         _________')
print('Discounted Total:        ', format(subTotal, ',.2f'))
print('Tax:                    +', format(taxAmount, ',.2f'))
print('                         _________')
print('Total amount to be paid $', format(totalAmount, ',.2f'))


# Enter the quantity of item sold: 80
# Enter the value of item : 100
# Enter the discount percentage: 10
# Enter the tax: 14
#
# *********BILL*********
# Quantity sold:               80.00
# Price per item:             100.00
#
#                          _________
# Amount:                   8,000.00
# Discount:               -   800.00
#                          _________
# Discounted Total:         7,200.00
# Tax:                    + 1,008.00
#                          _________
# Total amount to be paid $ 8,208.00
