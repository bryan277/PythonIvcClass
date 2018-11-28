#1. write a program to calculate the sum of numbers from m to n. Use a while loop.
# m = int(input('Enter the value of m: '))
# n = int(input('Enter the value of n: '))
#
# sum = 0
#
# while(m<=n):
#     m = m + 1
#     sum = sum + m
#
# print('Sum: ', )

#2. Write a porgram to read the numbers until -1 is encountered. Count the negatives, positive, and zeros entered by user.

# Enter -1 to exit
# Enter any number 10
# Count of positive numbers:6
# Count of negative numbers:3
# Count of zero numbers:1

num = int(input('Enter any number: '))

while num == -1:
    if num == 0:
        zero = zero + 1
    elif num > 0:
        pos = pos + 1
    else:
        neg = neg + 1

print('Count of positive numbers: ', pos)
print('Count of negative numbers: ', neg)
print('Count of zero numbers: ', zero)
#3. Write a program to read a char until a * is encountered. Count the number of uppercase, lowercase and number entered(0-9)

# if ch >= 'A' and ch <= 'Z':
#     print('upper')
# elif:


# 4. Write a program to enter a number and then calculate the sum of digits
# Enter a number: 1234
# The sum of digits = 10

#Write a program to determine if the given number is an Armstrong number armstrong number - sum of cues of its digits is equal to the number itself
