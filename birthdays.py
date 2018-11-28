#This program uses a dictionary to keep friends
#names and birthdays

#Global constanst for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#main functions
def main():
    #Create an empty dictionary
    birthdays = {}

    #Initialzie a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        #Get the user's menu choice.

        #Process the choice
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)

#The get_menu_choice function displays the menu
#and gets a validedate choice from the user
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()

    #Get the user's choice
    choice = int(input('Enter your choice: '))

    #Validate the choice.
    while choice 
