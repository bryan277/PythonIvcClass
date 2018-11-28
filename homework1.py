
#1003181
#CS10 Python Programming Homework 1

#Program Set 1 (10 points)
sugar = 1.50
butter = 1.00
flour = 2.75
cookies = 48.00

#formulas
sugarInput = sugar/cookies
butterInput = butter/cookies
flourInput = flour/cookies

#Input
inputCookies = float(input('Enter the number of cookies: '))
print('To make ' + format(inputCookies,'.1f') + ' cookies, you will need:' )
print(format(inputCookies*sugarInput, '.2f') + ' cups of sugar')
print(format(inputCookies*butterInput, '.2f') + ' cups of butter')
print(format(inputCookies*flourInput, '.2f') + ' cups of flour')

#Output
# Enter the number of cookies: 56
# To make 56.0 cookies, you will need:
# 1.75 cups of sugar
# 1.17 cups of butter
# 3.21 cups of flour
