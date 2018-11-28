#program allows user to input 3 values and calc sum and average

#input
name = input ("What's your name?")
num1 = int(input("Enter the first value"))
num2 = int(input("Enter the second value"))
num3 = int(input("Enter the third value"))

sum = num1 + num2 + num3
avg = sum/3

#Output
print("Your name is", name)
print("The 3 numbers are", num1, num2, num3)
print("The sum is", sum)
print("The average is", avg)
