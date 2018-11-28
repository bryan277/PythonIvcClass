#Example - write a program to convert celcius to Fahrenheit
#-user input
#Enter a celcius temperature
#Output
#That is equal to ____ degrees Fahrenheit
#Fahrenheit = 9/5 * celcius + 32
celcius = float(input("Enter a celcius temperature:"))
#conversion
Fahrenheit = 9/5 * celcius + 32
print("That is equal to " + format(Fahrenheit, '.2f') + "degress Fahrenheit")


#input
#Enter the amount of purchase:
#Output
#purchase amount:
# state tax:
# county tax:
# Total tax:
# State Total:

#state tax rate = 0.04
#county tax rate = 0.02

#state tax = Purchase amount * State tax rate
#county tax = Purchase amount * County tax rate
print("Enter the amount of purchase:")
purchase_amount = float(input())
state_tax = purchase_amount * 0.04
county_tax = purchase_amount * 0.02
total_tax = state_tax + county_tax
Sale_total = purchase_amount + total_tax

print("State tax:", format(state_tax, '.2f'))
print("County tax:", format(county_tax, '.2f'))
print("Total tax:", format(total_tax, '.2f'))
print("Sale Total:", format(Sale_total, '.2f'))
