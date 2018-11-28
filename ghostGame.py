import random

print('Ghoest Game')

brave = True
score = 0


while brave:
    ghost_door = random.randint(1,3)
    print("Three drops ahead")
    print("A ghost")
    print('What door do you open')
    door = int(input('1,2 or 3'))
    if door == ghost_door:
        print('Ghost')
        brave = False
    else:
        print('no ghost')
        score = score + 1
        print('Run Away!')
        print('Game Over, You Scored', score)
