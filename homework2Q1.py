
#1003181
#Due Oct 9
# Program Set 1(10 points) Lottery program.
import random

#Generates random from 0 to 99
randomNumber = random.randint(0,99)

#Guessing number from user
guessNumber = int(input('Please enter a two digit number? '))

#Formulas
lotteryDigit1 = randomNumber // 10 # Divides 10 by randomNumber which equals a number without decimals Ex. randomNumber = 89, lotteryDigit1 = 8
lotteryDigit2 = randomNumber % 10 # module Ex. randomNumber = 89, lotteryDigit2 = 9

guessDigit1 = guessNumber // 10
guessDigit2 = guessNumber % 10

print('The lottery number is: ', randomNumber)

if randomNumber == guessNumber:
    print('Your award is $10,000')
elif lotteryDigit1 == guessDigit2 and lotteryDigit2 == guessDigit1:
    print('Your award is $3,000')
elif (lotteryDigit1 == guessDigit1 or lotteryDigit1 == guessDigit2 or lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit2):
    print('Your award is $1,000')
else:
    print("Sorry you didn't win anything")


# Please enter a two digit number? 23
# The lottery number is:  30
# Your award is $1,000

# Please enter a two digit number? 23
# The lottery number is:  59
# Sorry you didn't win anything

# Please enter a two digit number? 23
# The lottery number is:  13
# Your award is $1,000

# Please enter a two digit number? 23
# The lottery number is:  34
# Your award is $1,000

# Please enter a two digit number? 23
# The lottery number is:  1
# Sorry you didn't win anything

# Please enter a two digit number? 23
# The lottery number is:  27
# Your award is $1,000

# Please enter a two digit number? 23
# The lottery number is:  86
# Sorry you didn't win anything
