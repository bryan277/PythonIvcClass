# Global - can be accessed everywhere in the program
# Local - can only be accessed where it is declared, example a function

#Avoid global variables -> gives side effects

# example 1

globalVar = 1

def f1():
    localVar = 2
    print(globalVar)
    print(localVar)

f1()
print(globalVar)
print(localVar) # doesn't work

# example 2

x = 1
def f1():
    x = 2
    print(x)

f1()

# example 3
x = int(input('Enter a number'))
if x > 0:
    y = 4

print(y)
#if y is less than zero y is out of scope

# example 4
sum = 0

for i in range(5):
    sum += i

print(i)

# example 5
x = 1

def iner():
    global x
    x = x + 1
    print(x)

iner()

# x is global and bound in function in lime3 -> means x in function is same as x in global.
