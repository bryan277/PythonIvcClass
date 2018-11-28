numbers = int(input('How many numbers do you want to add? ' ))
total = 0

for num in range(numbers):
    enterNumber = int(input('Enter number ' + str(num + 1) + ': ' ))
    total += enterNumber

print('The total is : ', total)

# Enter number 1:10
# Enter number 2:10
# Enter number 3:10
# The total is :  30
