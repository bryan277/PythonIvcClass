#1ask user to input first, last name, id
#create a login name

#2.function to test if password is valid
# -must have at least 7 char long
# -must contain at least one uppercase
# -must contain at lest one lowercase
# -at least one numeric digit

def main():
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    id_num = input('Enter id number: ')

    print('You system login name is')
    print(get_login_name(first, last, id_num))

#check password
password = input('Enter password')
while not valid_password(password):
    print('Password not valid')
    password = input('Enter password')
print('Valid password')


def get_login_name(first, last, id_num):
    return first[:3] + last[:3] + id_num[-3:]

print(get_login_name('Hans', 'Voss', '123456789'))



def valid_password(password:str):
    # len()
    # isupper()
    # islower()
    # isdigit()
    correct_length = False
    hasUppercase = False
    hasLowercase = False
    hasDigits = False
    #test passwrod length
    if len(password) > 7:
        correct_length = True
    # test for
    for ch in password:
        if ch.isupper():
            hasUppercase = True
        if ch.islower():
            hasLowercase = True
        if ch.isdigit():
            hasDigits = True

if correct_length and hasUppercase and hasLowercase and hasDigits:
    is_valid = True
else:
    is_valid = False
return is_valid

main()


name = 'Timothy'

for x in name:
    print(x)

#Program to count number of times of T appears in a string entered by user
def numberOfTees():
    total = 0
    my_string = input('Enter a string')
    for ch in my_string:
        if ch == 'T' or ch == 't':
            total += 1

print('Letter t appears ', total, 'times')
numberOfTees()


#splitting a string
def main():
    my_string = 'One Two Three Four'
    word_list = my_string.split()
    print(word_list)

main()
# ['One', 'Two', 'Three', 'Four']

date_string = '11/26/2018'
date_list = date_string.split('/')
print('Month: ', date_list[0])
print('Day: ', date_list[1])
print('Year: ', date_list[2])


print(date_list)
# Month:  11
# Day:  26
# Year:  2018
# ['11', '26', '2018']
