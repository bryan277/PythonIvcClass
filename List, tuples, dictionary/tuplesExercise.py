# 1. Write a Python program to create a tuple.
x = ()
print(x)
tuplex = tuple()
print(tuplex)
# ()
# ()

# 2. Write a Python program to create a tuple with different data types.
tuples = (False, 1, '1', 'Hey')
print(tuples)
# (False, 1, '1', 'Hey')

# 3. Write a Python program to create a tuple with numbers and print one item.
tuplex = 5, 10, 15, 20, 25
print(tuplex)
tuplex = 5,
print(tuplex)
# 2
(5, 10, 15, 20, 25)
(5,)

# 4. Write a Python program to unpack a tuple in several variables.
tuplex = 4, 8, 3
print(tuplex)
# (4, 8, 3)
n1, n2, n3 = tuplex
#unpack a tuple in variables
print(n1, n2, n3)
# 4 8 3
n1, n2, n3, n4 = tuplex
# ValueError: not enough values to unpack (expected 4, got 3)

# 5. Write a Python program to add an item in a tuple.
# create a tuple
tuplex = (4,6,2,8,3,1)
print(tuplex)
tuplex = tuplex = (9,)
print(tuplex)

# 6. Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)
