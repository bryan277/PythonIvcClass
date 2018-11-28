#Tuples
#A tuple is an immutable sequence, - comments cannot be changed
my_tuple = (1,2,3,4,5)
print(my_tuple)
# (1, 2, 3, 4, 5)

for n in my_tuple:
    print(n)
# 1
# 2
# 3
# 4
# 5
names = ('Holly', 'Warren', 'Ashley')

for i in range(len(names)):
    print(names[i])
# Holly
# Warren
# Ashley

# Create a tuple with a style element
my_tuple = (1, )

#So, if tuples same as lists except immutable, why use tuple?

# 1.tuples process faster
# 2.good for lots of data
# 3.supports all list operations but not append, remove, insert, revise, sort

#Convert between lists and tuple
num_tuple = (1,2,3)
num_list = list(num_tuple)

list1 = [1,2,3]
tup = tuple([list])
