#Random Numbers
#using randint() and randrange() - returns and integer random numbers

#Ciaps Reller Game
#Demostrate random number generation

import random

#generate random numbers 1-6
die1 = random.randint(1,6) #dot is excess
die2 = random.randrange(6) + 1 #we are adding 1 because there is no zero in dice

total = die1 + die2
print("you rolled a", die1, "and a", die2, "a total o f", total)

#1.import random - import statment leads the random module
#2.modules - files that contain codes that are grouped together that are to be used in others program eg. all modules related to random
#3.modulename.functionname.() -> random.randint(1,6)
#4.randint(start, end)
#5.randrange(n) -> pick n numbers starting from y to n-1
#num = randrange(10) -> 0 1 2 3 4 5 6 7 8 9
#num = randrange(5, 10) -> 5 6 7 8 9
#num = randrange(0, 10, 10) -> 0 10 20 30 .......
