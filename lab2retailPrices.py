cost = float(input("Enter the item's wholesale cost: " ))
item = 'y'

while item != 'n':
    if cost < 0:
        print('ERROR: the cannot be negative')
        cost = float(input('Enter the correct wholesale cost: '))
        print('Retail price is: ', cost*2.5)
    else:
        print('Retail price is: ', cost*2.5)
    item = str(input('Do you have another item? (Enter y for yes): '))


for times in range(5):
    print('Barzinger')
