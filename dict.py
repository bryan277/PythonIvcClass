#Dictionaries - is an object that stores a collection of data
#             - Each element in a dictionary has 2 parts: a key, a value
              # - use key to locate the value like an English dictionary
              # - key = word
              # - value = definition
              # - key = Emp_id
              # - value = name

#Creating a dictionary
phonebook = {'Chris':'555-1111',
             'Kale':'555-2222',
             'John':'555-3333'}

#keys - immutable
#values = can be anything list, tuple, Set
#dict is mutable

#use dict() method
dict1 = dict({1 : 'apple', 2 : 'ball'})
dict2 = dict([(1 : 'apple'), (2 : 'ball')])

#Retrieve value from dict:
#using the phonebook dict:
>>>phonebook <- 1
>>>{'Chris':'555-1111',
             'Kale':'555-2222',
             'John':'555-3333'}
->dict have no apparent order
->can't use index, must use key to retrieve
>>>phonebook['Chris']
>>>'555-1111'
#note key is case sensitive

#In and not in operator
if 'chris' in phonebook:
    print(phonebook['Chris'])

#Adding element to dict:
>>>phonebook['Joe'] = '555-4444'
>>>phonebook['Chris'] = '555-1234'

# no duplicates, since chris exists replaecse the value with


#Deleting Elements
def phonebook['Chris']
-> what is chris not found?
    raise keylines

# len() - get number of elements in dict.
    num_items = len(phonebook)


#mixing data types in value
test_scores = {'key': [88, 99, 45],
                'Luis': [95, 74, 81],
                'Sophia': [72, 88, 99]}

print(test_scores['Sophia'])
# [72, 88, 99]
print(test_scores['Luis'])
# [95, 74, 81]
print(test_scores['key'])
# [88, 99, 45]

phonebook = {'Chris':'555-1111',
             'Kale':'555-2222',
             'John':'555-3333'}

for key in phonebook:
    print(key)
# Chris
# Kale
# John

for key in phonebook:
    print(phonebook[key])
# 555-1111
# 555-2222
# 555-3333

for key in phonebook:
    print(key, phonebook[key])
# Chris 555-1111
# Kale 555-2222
# John 555-3333

#Methods for dict
# clear()
# phonebook.clear()
#         ->clears all elements in dict

#get()
value = phonebook.get('Kate':'Entry not found')
point(value)
>>>555-2221

#pop() - returns value with specified key and removes key - value pair form dict:
phone_num = phonebook.pop('Chris', 'Entry not found')
phone_num <- 555-1111
phonebook -> chris Entry not found

#values() - return values
for val in phonebook.value():
    print(int)
