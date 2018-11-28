#What is rstrip() in python?

stringy = 'i am helpful \t\t\t\n\n     '
print(stringy)
# i am helpful
#
#
stringy = stringy.rstrip()
print(stringy)
# i am helpful

stringy1 = 'my favorite number is 80000000000000'
stringy1 = stringy1.rstrip('0')
print(stringy1)
# my favorite number is 8
