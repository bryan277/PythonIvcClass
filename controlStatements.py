#Control Statments(disicion statments)

# if statement
    # -Q disicion structure
    # -allows c program to have more than one path
    # -causes one or more statment to execute only when a boolean expression is True

# if the condition is tested True
#     then the statements are executed
# if not true, they are skipped

#Example
sales = 5001
if sales > 5000.00:
    #bonus * 500
    #commission_rate * 0.12
    print('You met your sales quota!')

print('You did not met the quota')

#Relational operators
# >  #greater than
# <  #less than
# >= #greater than or equal
# <= #less than or equal
# == #equal (comparison)
# != #not equal

#Write a program to calculate the average of 3 test scores
#The grading are as follows
#if the average is 90 or greater A
#80 to 89 B
#70 to 79 C
#69 and below F

#input
test1 = int(input('Enter test 1'))
test2 = int(input('Enter test 2'))
test3 = int(input('Enter test 3'))

avg = (test1 + test2 + test3)/3

#comparison
if (90 <= avg <= 100):
    print('A')
elif(80 <= avg <= 89):
    print('B')
elif(70 <= avg <= 79):
    print('C')
elif(60 <= avg <= 69):
    print('D')
elif(avg < 59):
    print('F')
else:
    print('not a number')


#Logical operators (2 ore more conditional expression)
#and
x > y and a < b
#or
x == y or x == z
#not


#Truth table
# True and True = true
# True and False = False
# False and False = False
# True or True = true
# True or False = True
# False or False = False
# not(False)= True
# not(true)= False

temp = 101

if not(temp > 100):
    print('false')

avg = 101

if avg >= 90 and avg <= 100:
    print('A')
if avg >= 80 and avg <= 89:
    print('B')
if avg >= 70 and avg <= 79:
    print('C')
if avg <= 69:
    print('F')
if avg < 0 or avg > 100:
    print("out of range")
