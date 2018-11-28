def main():
    print('Enter three names of 3 friends')
    name1 = input('Enter #1')
    name2 = input('Enter #2')
    name3 = input('Enter #3')
    mgfile = open('friends.txt', 'w')
    mgfile.write(name1 + '\n')
    mgfile.write(name2 + '\n')
    mgfile.write(name3 + '\n')
    print('names written to file')

main()
