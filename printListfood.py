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
        item_index = food.index(item)

        #Get the value to replace it with
        new_item = input('Enther the new value: ')

        #Replace the old item with the new item:
        food[item_index] = new_item

        #Display the list
        print('here is the revised list')
        print(food)
    except ValueError:
        print('That item use not found in the list')

#Call the main function
main()
