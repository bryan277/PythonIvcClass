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
