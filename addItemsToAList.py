#Program to add items to a list
def main():
    name_list = [] #or name_list = list()
    again = 'T'
    while again.upper() = 'T':
        name = input('Enter a name')
        name_list = append(name)
        print('Do you want add another name?')
        again = input('y = yes, n = no')

print('Here are the names you entered')

for name in name_list:
    print(name)

if __name__=="__main__":
    main()
