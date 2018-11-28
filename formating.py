#Formatting numbers
#format specifier
format(123456, )

print(format(12345.6789, '.2f'))
#12345.68
print(format(12345.6789, '.1f'))
#12345.7
print("The number is",format(1.234567,'.2f'))
#The number is 1.23

#Insert commas
print(format(12345.6789, '.2f'))
#12345.68

#The precision set
print(format(12345.6789,'f'))
#12345.678900

#Width specifier
print("The number is $", format(12345.6789,'12.3f'))

print('Property tax: ${:,.2f}'.format(1234.5))
#$1,234.50

print("{:<13}$ {:>7.2f}".format("Total", 7.34))
