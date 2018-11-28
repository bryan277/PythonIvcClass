#Hans Vos
#1003181
#CS Python Programming Homework 2 Set 4

#input from user
income = int(input('Enter income as an integer with no commas: '))


#2017 income range and it's precentage rate
while income > 0:#it quits the program if user inputs any negative number
    if income <= 9325:
        tax2017 = income * .10
    elif 9325 <= income <= 37950:
        tax2017 = 9325 * .10 + ((income-9325)*.15)
    elif 37951 <= income <= 91900:
        tax2017 = 9325 * .10 + ((37950-9325)*.15) + ((income-37950) * .25)
    elif 91901 <= income <= 191650:
        tax2017 = 9325 * .10 + ((37950-9325)*.15) + ((91900-37950) * .25) + ((income-91900) * .28)
    elif 191651 <= income <= 416700:
        tax2017 = 9325 * .10 + ((37950-9325)*.15) + ((91900-37950) * .25) + ((191650-91900) * .28) + ((income -191650) * .33)
    elif 416701 <= income <= 418400:
        tax2017 = 9325 * .10 + ((37950-9325)*.15) + ((91900-37950) * .25) + ((191650-91900) * .28) + ((416700-191650) * .33) + ((income-416700) * .35)
    elif income >= 418401:
        tax2017 = 9325 * .10 + ((37950-9325)*.15) + ((91900-37950) * .25) + ((191650-91900) * .28) + ((416700-191650) * .33) + ((418400-416700) * .35) + ((income - 418400) * .396)

#2018 income range and it's precentage rate
    if income <= 9525:
        tax2018 = income * .10
    elif 9526 <= income <= 38700:
        tax2018 = 9525 * .10 + ((income-9525)*.12)
    elif 38701 <= income <= 82500:
        tax2018 = 9525 * .10 + ((38700-9525)*.12) + ((income-38700) * .22)
    elif 82501 <= income <= 157500:
        tax2018 = 9525 * .10 + ((38700-9525)*.12) + ((82500-38700) * .22) + ((income-82500) * .24)
    elif 157501 <= income <= 200000:
        tax2018 = 9525 * .10 + ((38700-9525)*.12) + ((82500-38700) * .22) + ((157500-82500) * .24) + ((income -157500) * .32)
    elif 200001 <= income <= 50000:
        tax2018 = 9525 * .10 + ((38700-9525)*.12) + ((82500-38700) * .22) + ((157500-82500) * .24) + ((200000 -157500) * .32) +((income-200000) * .35)
    elif income >= 500000:
        tax2018 = 9525 * .10 + ((38700-9525)*.12) + ((82500-38700) * .22) + ((157500-82500) * .24) + ((200000 -157500) * .32) +((500000-200000) * .35) + ((income - 500000) * .37)

#output
    print('Income: ', income)
    print('2017 tax: ', tax2017)
    print('2018 tax: ', tax2018)
    print('Difference: ', '%.2f' % (tax2018 - tax2017))
    print('Difference (percent): ', '%.2f' % (((float(tax2017) - tax2018)/abs(tax2018))*100))
    income = int(input('Enter income as an integer with no commas: '))
    print()


# Enter income as an integer with no commas: 8000
# Income:  8000
# 2017 tax:  800.0
# 2018 tax:  800.0
# Difference:  0.00
# Difference (percent):  0.00
#
# Enter income as an integer with no commas: 15000
# Income:  15000
# 2017 tax:  1783.75
# 2018 tax:  1609.5
# Difference:  -174.25
# Difference (percent):  10.83
#
# Enter income as an integer with no commas: 40000
# Income:  40000
# 2017 tax:  5738.75
# 2018 tax:  4739.5
# Difference:  -999.25
# Difference (percent):  21.08
#
# Enter income as an integer with no commas: 100000
# Income:  100000
# 2017 tax:  20981.75
# 2018 tax:  18289.5
# Difference:  -2692.25
# Difference (percent):  14.72
#
# Enter income as an integer with no commas: 200000
# Income:  200000
# 2017 tax:  49399.25
# 2018 tax:  45689.5
# Difference:  -3709.75
# Difference (percent):  8.12
#
# Enter income as an integer with no commas: 500000
# Income:  500000
# 2017 tax:  153818.85
# 2018 tax:  150689.5
# Difference:  -3129.35
# Difference (percent):  2.08
#
# Enter income as an integer with no commas: 1000000
# Income:  1000000
# 2017 tax:  351818.85
# 2018 tax:  335689.5
# Difference:  -16129.35
# Difference (percent):  4.80
#
# Enter income as an integer with no commas: 10000000
# Income:  10000000
# 2017 tax:  3915818.85
# 2018 tax:  3665689.5
# Difference:  -250129.35
# Difference (percent):  6.82
# Enter income as an integer with no commas: -1
