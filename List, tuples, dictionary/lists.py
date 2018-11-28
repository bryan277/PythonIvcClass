#a list of values.
#List are similar to tuples. mutable - values can be be changed. Most of the time we use lists, not tuples.
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

print(cats[2])
# Kitty
cats.append('Catherine')
print(cats)
# ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester', 'Catherine']
print(cats[1])
del cats[1]
# Snappy
print(cats)
# ['Tom', 'Kitty', 'Jessie', 'Chester', 'Catherine']
for cats in cats:
    print(cats)
# Tom
# Kitty
# Jessie
# Chester
# Catherine

if 'Tom' in cats:
    print("Yes, 'Tom' is in the fruits list")

# print(len(cats))
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

cats.insert(1, 'Jerry')
print(cats)
# ['Tom', 'Jerry', 'Snappy', 'Kitty', 'Jessie', 'Chester']
cats.insert(2, 'Kobe')
print(cats)
# ['Tom', 'Jerry', 'Kobe', 'Snappy', 'Kitty', 'Jessie', 'Chester']
cats.remove('Tom')
print(cats)
# ['Jerry', 'Kobe', 'Snappy', 'Kitty', 'Jessie', 'Chester']
cats.remove('Snappy')
print(cats)
# ['Jerry', 'Kobe', 'Kitty', 'Jessie', 'Chester']
cats.pop()
print(cats)
# ['Jerry', 'Kobe', 'Kitty', 'Jessie']
cats.pop()
print(cats)
# ['Jerry', 'Kobe', 'Kitty']
del cats[0]
print(cats)
# ['Kobe', 'Kitty']
del cats[1]
print(cats)
# ['Kobe']

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
del cats
print(cats)#this will cause an error because "thislist" no longer exists.

cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
cats.clear()
print(cats)
# []

cats = list(('Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester'))
print(cats)
# ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']

#update
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
# {'mango', 'apple', 'orange', 'banana', 'grapes', 'cherry'}
