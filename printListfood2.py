def main():
    # create a list with some items:
    food = ['Pizza', 'Burgers', 'Chips']

    #Display the list
    print('THe are the items in the food list')
    print(food)

    # Get the item to change
    item = input('Which item should I change')

    try:
        #Get the item's index in the list
        food.remove(item)

        #Get the value to replace it with
        print('These is the revised list.')
        print(food)

    except ValueError:
        print('That item use not found in the list')

#Call the main function
main()


def main():
    # Create a list with some names
    names = ['James', 'Kathryn', 'Bill']

    #Display the list
    print('The list reduce  the insert')
    print(names)

    #insert a new anem at element 0.
    names.insert(0, 'Jeo')

    #Display the list again
    print('the list after teh insert')
    print(names)

#Call the main function
main()
