#Ask user for base size? 4
# *
# **
# ***
# ****
# ****
# ***
# **
# *
#For loop

#number of base
base_size = int(input('Enter triangle base'))

for row in range(base_size):
    for col in range(row + 1):
        print('*', end='')
    print()
