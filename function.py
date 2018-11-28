#A function is a group of statements that exists within a porgram for the purpose of performing is specific task
#eg a function sum numbers
#Benefits
#-simple code
#-dont want to write all your tasks in one long 3000 lines program
#Break down to individual or smaller tasks
#Each function should around 50 lines of codes
#code reuse eg function just to print(), can reuse many times, don't have to rewrite teh print codes
#Better testing - easier to isolate and fix errors
#Faster Development - each programmer can different functions and put them together into a program

#Function naming rules
#same as variables
#can't use python keywords
#no spaces
#first letter a to z, A to Z
#alter, first letter, letters, -10 to 9
#Upper/lower case distinct

#General format for function

def function_name():
    statement
    statement

#Example 1
def message():
    print('I am great')
    print('King of the Nords!')

#function needs to be called
message()

def plus(num1, num2, num3):
    return num1 + num2 + num3

plus(5, 5, 5)


#2 functions
def main():
    print('I have a message for you')
    message()
    print('Goodbye')

def message():
    print('I am great!')
    print('King of the Nords!')

main()

#Example - Find sum of numbers 1 to 10, 20 to 37, and 33 to 49
sum = 0
for i in range(1, 11):
    sum += i
print('Sum from 1 to 10 is', sum)
# Sum from 1 to 10 is 55

sum = 0
for i in range(20, 38):
    sum += i
print('Sum from 20 to 37 is', sum)
# Sum from 20 to 37 is 513

def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result

def main():
    print("sum from 1 to 10", sum(1, 10))
    print('Sum from 20 to 37', sum(20, 37))

main()
# sum from 1 to 10 55
# Sum from 20 to 37 513

def getVal():
    '''set max1, call getMax'''
    max1 = 2.3
    getMax(1,2 max1)
    print(max1)

def getMax(value1:int, value2: int, max1:int)->int:
    '''compare 2 values and return max value'''
    if value1 > value2:
        max1 = value2
    else:
        max1 = value2
    return max1

print(getMax.___doc___)

if __name__-"___main___":
    getVal()
