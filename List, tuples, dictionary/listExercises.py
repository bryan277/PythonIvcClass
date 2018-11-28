# 1. Write a Python program to sum all the items in a list.
def sum_list(items):
    list1 = 0;
    for x in items:
        list1 += x
    return list1
print(sum_list([1,2,3,4]))
# 10

# 2. Write a Python program to multiplies all the items in a
def multiplies_list(items):
    list1 = 1;
    for x in items:
        list1 *= x
    return list1
print(multiplies_list([1,2,3,4]))
# 24

# 3. Write a Python program to get the largest number from a list.
def largest_list(items):
    max = items[0]
    for a in items:
        if a > max:
            max = a
    return max
print(largest_list([1,2,3,4]))
# 4

# 4. Write a Python program to get the smallest number from a list.
def smallest_list(items):
    min = items[0]
    for a in items:
        if a < min:
            min = a
    return min
print(smallest_list([1,2,3,4]))
# 1
