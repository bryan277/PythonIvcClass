# 2.Write a program to create a list of numbers in the range of 1 to 10.
# Then delete all the even numbers from the list and print the final list.
# def makeList() – function to create the list of numbers from 1 to 10
# def delEven() – function to delete even numbers from list
# def main()- call the above functions and print
# Original List – [1,2,3,4,5,6,7,8,9,10]
# List after deleting even numbers: [1,3,5,7,9]

# listNum = list(range(1,11))
# print(listNum)

# def makeList(arr):
#     arr = str(range(1,11))
#
# def delEven(l):
#     for i in l[:]:
#         if i % 2 == 0:
#             l.remove(i)
#     return l
#
#
# def main():
#     listNum = []
#     print('Original List: ' + listNum)
#     print('Deleting even numbers: ' + delEven(listNum))


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
