#strings
#functions for strings
# len(), max(), min()
#
# s = 'Welcome'
#
# print(len(s))
#
# print(max(s))
#
# index operator []
#
# s = 'Welcome'
# for i in range(0,len(s), 2):
#     print(s[i], end = 'y')

# s[0] = W

#STRINGS ARE IMMUTABLE(cannot be changed)

#S[2] = 'A' is illegal since S[2] = l

# word = 'index'
# print('The word is: ', word, '\n')
#
# high = len(word)
# low = len(word)
#
# for i in range(10):
#     pos = random.randrange(low, high)
#     print(word["pos"]"t\", word[pos])

#string operator [start:end]

s = 'Welcome'
print(s[1:4])
#elc
print(s[:6])
# Welcom
print(s[0:6])
# Welcome
print(s[4:])
#ome
print(s[1:-1])
#elcom

#Contenation and repetition
s1 = 'Welcome'
s2 = 'Python'
s3 = s1 + 'to' + s2

print(s3)
#WelcometoPython

#The in and not in operators
s1 = 'Welcome'
    "come" in s1
>>>True

    "come" not in s2
>>>False

# Example
s = input('Enter a string')
if "Python" in s:
    print('Python is in', s)

#string methods
stringvar.method(arguments)

isalnum() #True if string contains only alphabetic letter or digits and at least one cher in length

isalpha() #True if all letters

isdigit() #True if all digits

islower() #True if all letter are lowercase

isupper() #True if all letter are uppercase

isspace() #True if string contains only whitespace character \n tabs spaces

#Example
string1 = '1200'
if string is digit():
    print(string1, 'contains only digits')
else:
    print(string, 'contains char character')

lower()
upper()
strip()#returns copy of strings with all leading and trailing whitespace removed


again = 'y'

while again.lower() == 'y':
    print('hello')
