#InterSection and operators
a_set = {'a', 'b', 'c', 'd'}
b_set = {'c', 'd', 'e', 'f'}

a_set & b_set
{'c', 'd'}

a_set.intersection(b_set)

#Union
a_set | b_set
{'a', 'b', 'c', 'd', 'e', 'f'}

b_set | a_set

a_set.union(b_set)

#Difference
Order matters, net commutative

a_set = {'a', 'b', 'c', 'd'}
b_set = {'c', 'd', 'e', 'f'}

a_set - b_set
{'a', 'b'}

b_set - a_set
{'e', 'f'}

Symmetric Difference
a_set ^ b_set
{'a', 'b', 'e', 'f'}

b_set ^ a_set
a_set.Symmetric_difference(b_set)

subset/superset

small_set = {'a', 'b', 'c'}
big_set = set('abcdef')

small_set <= big_set
