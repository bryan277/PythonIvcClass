#1. pick 1-100
#2.  user input guess
#3. compare random number with user guess
#if number = guess
#if not -> tell user higher or lower

#Guess my number game 1-100
import random

print('Guess my number between 1 to 100')
#random value
my_number = random.randint(1, 100)
guess = int(input('Take a guess'))
count = 1
#loop
while guess = my_number:
    if guess > my_number:
        print('guess lower')
    else:
        print('guess higher')
    count = count + 1
    guess = int(input("Take a guess"))

print("You guess it. The number is", my_number)
print("You took", count, "tries")
