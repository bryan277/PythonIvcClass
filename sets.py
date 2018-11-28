#Sets
#=sets are like lists for storing a collection of elements
#-unlike lists, the elements in a set are non-duplicates
#-elements are not ordered
#use sets if order of elements not important, more of efficient
#sets are mutable

S1 = set()  #create empty set
S2 = {1,3,5} #create a set with 3 elements
S3 = set([1,3,5])
#conversion
list(set)
tuple(set)
#create set from a string
s5 = set('abac')
print(s5)
# {'c', 'b', 'a'}


my_set = set('one', 'two', 'three')#not allowed, set function only allow one argument
my_set = set('one two three')
print(my_set)
# {' ', 'h', 'e', 'r', 't', 'o', 'w', 'n'}

my_set = set(['one', 'two', 'three'])
print(my_set)
# {'two', 'three', 'one'}
