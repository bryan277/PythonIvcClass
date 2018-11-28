# Default arguments
# Default arguments are passed to the parameters when a function is invoked without arguements
#
#

def printArea(width = 1, height = 2):
    area = width * height
    print('width:', width, 'height:', height, '\tarea', area)

#function call
printArea()
printArea(4, 2.5)


printArea(width = 1.2)
printArea(height = 6.2)

#keyword argument

def f1(P1, P2, P3):


#function call
f1(30, P2= 4, P3= 10)
f1(30, P2=4, 10) #not good position
