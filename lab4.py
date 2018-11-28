# 1.Write a program that  a.defines a list of countries that are members of BRICS (Brazil, Russia, India, China, Sri Lanka)
# b.Check whether a country is a member of BRICS or not
# Program run Enter the name of country:
# Pakistan Pakistan is not a member of BRICS
# Enter the name of country :
# India India is a member of BRICS
brics = ['Brazi', 'Russia', 'India', 'China', 'Sri Lanka']



def main():
    userInput = input('Enter the name of country: ')
    if brics == str(userInput):
        print(str(userInput) + ' is a member of BRICS')
    if brics != str(userInput):
        print(str(userInput) + ' is not a member of BRICS')

main()

# 2.Write a program to create a list of numbers in the range of 1 to 10.
# Then delete all the even numbers from the list and print the final list.
# def makeList() – function to create the list of numbers from 1 to 10
# def delEven() – function to delete even numbers from list
# def main()- call the above functions and print
# Original List – [1,2,3,4,5,6,7,8,9,10]
# List after deleting even numbers: [1,3,5,7,9]

# listNum = list(range(1,11))
# print(listNum)

def makeList():
    listNum = list(range(1,11))
    print('Original List: ' + str(listNum))

def delEven(l):
    for i in l[:]:
        if i % 2 == 0:
            l.remove(i)
    return l


def main():
    listNum = list(range(1,11))
    makeList()
    print('List after deleting even numbers : ' + str(delEven(listNum)))

main()
# Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List after deleting even numbers : [1, 3, 5, 7, 9]

# 3.Write a program to remove all duplicates from a list.
# a.def createList()- allow the user to input data into the list
# b.def removeDuplicates() – function will remove duplicates
# c.def main()- call the above functions and print
# program run: Original List : [1, 2, 3, 4, 5, 6, 7, 6, 5, 4]
# List after removing duplicates : [1, 2, 3, 4, 5, 6, 7]
def createList():
    listNum = input('Input list: ')
    return listNum

def removeDuplicates(lis):
    return set(lis)

def main():
    createList()
    removeDuplicates(listNum)

main()

# 4.write a program that creates a tuple of numbers(both positive and negative).
# Make a new tuple that has only positive values from this tuple and sort it in descending order.
# Tup = (-10, 1, 2, -9, 3, 4, -8, 5, 6) Program run: Original
# Tuple : (-10, 1, 2, -9, 3, 4, -8, 5, 6) New Tuple with Positive numbers : (1, 2, 3, 4, 5, 6)
Tup = (-10, 1, 2, -9, 3, 4, -8, 5, 6)
#
# def newTuple(arr):
#     return [x for x in arr if x > 0] or None
def pos(lst):
    return [x for x in lst if x > 0] or None
# print('Original Tuple: ' + Tup)
# print('New Tuple with Positive numbers: ' + str(newTuple(Tup))
print('Original Tuple : ' + str(Tup))
print('New Tuple with Positive numbers ' + str(pos(Tup)))
# Original Tuple : (-10, 1, 2, -9, 3, 4, -8, 5, 6)
# New Tuple with Positive numbers [1, 2, 3, 4, 5, 6]



# 5.Write a program using list to read a sequence of values and prints them, and highlighting the largest number.
# These are the required functions
# a.def readValues() – to read in a series of floats by the user into a list.
# b.def findLargest()- pass the list into the function and find largest
# c.def display() – display the list and highlight the largest d.use a main function to call the above functions
# program run:
# Please enter values, Q to quit: 34 56.7 4 9 76.9 55.4 Q
# Here are the numbers in the list 34 56.7 4 9
# 76.9 <== this is the largest number 55.4
