# 5.Write a program using list to read a sequence of values and prints them, and highlighting the largest number.
# These are the required functions
# a.def readValues() – to read in a series of floats by the user into a list.
# b.def findLargest()- pass the list into the function and find largest
# c.def display() – display the list and highlight the largest d.use a main function to call the above functions
# program run:
# Please enter values, Q to quit: 34 56.7 4 9 76.9 55.4 Q
# Here are the numbers in the list 34 56.7 4 9
# 76.9 <== this is the largest number 55.4

def readValues():
    values = (input(float('Please enter values, Q to quit: ' )))
    return list(values)
    if (values == 'Q'):
        break;

# def findLargest():
#
# def display():
#
# def main():
#     readValues()
#     findLargest()
#     display()

# values = input(float('Please enter values, Q to quit: ' ))
# print(values)

values = float(input('Please enter values, Q to quit: '))
print(str(values))
