# 1 Input/Data
# Computer random scissor 0
#                 rock 1
#                 paper 2
#user iput 0,1 or 2
# 2 Proccessing/Output

#comparsion if statement

#Possibility chart
#Computer  User   userinput  Score
#   0       0        D         -
#           1        W         +1
#           2        L         -1
#   1       0        L         -1
#           1        D         -
#           2        W         +1

import random

count = 0

while count <= 2 and count >= -2:
    compNum = random.randint(0,2)
    userNum = int(input('Scissor(0), Rock(1), Paper(2)'))
    if compNum == 0:
        if userNum == 0:
            print('Draw')
        elif userNum == 1:
            print('You win')
            count = count + 1
        elif userNum == 2:
            print('You lose!')
            count = count - 1
    elif compNum == 1:
        if userNum == 0:
            print('You lose')
            count = count - 1
        elif userNum == 1:
            print('Draw')
        elif userNum == 2:
            print('You win')
            count = count + 1
    elif compNum == 2:
        if userNum == 0:
            print('win')
            count = count + 1
        elif userNum == 1:
            print('lose')
            count = count - 1
        elif userNum == 2:
            print('Draw')
    if count > 2:
        print('You win')
    else:
        print('You lose')
