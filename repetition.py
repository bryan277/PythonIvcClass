#Reptition(10ps)
#2 main types of loops
#1. condition controlled -> while
#2. counter controlled -> for

hungry = true
#while
while hungry:
    print('eat a lobster')

#2 parts to a while loop
#1.condition to test for true/false
#2.statment repeated if condition true
#Example:
x = 0
while x < 10:
    print(x, end='b')
    x = x + 1
print()
print("Final value of x:", x)
# 0b1b2b3b4b5b6b7b8b9b
# Final value of x: 10

#Example2
#Temperature check Program
may_temp = 102.5

temp = float(input("Enter a temperature"))
while temp > may_temp:
    print('The temperature is to high')
    print('Turn on air con')
    temp = float(input("Enter a temperature"))

print("Temperature is cooler")
print("Check again in 30 min")
