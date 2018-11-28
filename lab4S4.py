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
