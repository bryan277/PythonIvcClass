
#1003181
#CS10 Python Programming Homework 1

#Program Set 2 (10 points)
#input
annualInterestRate = float(input('Enter annual interest rate, e.g., ' ))
numberOfYears = float(input('Enter number of years as an integer, e.g., ' ))
loanAmount = float(input('Enter loan amount, e.g., ' ))

#formulas
monthlyInterestRate = annualInterestRate/(100*12)
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears * 12

print('The monthly payment is ' + format(monthlyPayment, '.2f'))
print('The total payment is ' + format(totalPayment, '.2f'))

#Output
# Enter annual interest rate, e.g., 7.25
# Enter number of years as an integer, e.g., 5
# Enter loan amount, e.g., 120000.95
# The monthly payment is 2390.34
# The total payment is 143420.54
