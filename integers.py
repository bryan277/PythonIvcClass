#Format integer
print(format(12345,'10,d'))
#    12,345

#Formatting floating point as percentage
print(format(0.5, '%'))
#50.000000%
print(format(0.5,'.%'))
#
print(format(0.5,'.2%'))
#50.00%

#program currency
pay = 5000.0
yearly_pay = pay * 12
print("Your annual pay is $",format(yearly_pay,',.2f'),sep='')
#Your annual pay is #60,000.00
#sep = ' '

#More data output
print('one')
print('two')
print('three')
# one
# two
# three
print('One', end='')
print('Two', end='')
print('Three')
#OneTwoThree
print('one','two','three')
#one two three
print('one', 'two', 'three', sep='*')
#one*two*three
print('one', 'two', 'three', sep= '')
#onetwothree
