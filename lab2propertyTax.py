lotNumber = int(input('Enter the property lot number or enter -999 to end '))

while lotNumber != -999:
    print('Enter the lot number: ', lotNumber)
    propertyValue = float(input('Enter property value: '))
    print('Property tax: ${:,.2f}'.format(propertyValue * 0.0065))
    lotNumber = int(input('Enter the property lot number or enter -999 to end'))

# Enter the property lot number or enter -999 to end100
# Enter the lot number:  100
# Enter property value: 1000000.00
# Property tax: $6,500.00
# Enter the property lot number or enter -999 to end200
# Enter the lot number:  200
# Enter property value: 5000.00
# Property tax: $32.50
# Enter the property lot number or enter -999 to end-999
