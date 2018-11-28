# def sumOfDoubleEvenPlace(num): # Get the result from Step 2
#     length = len(num)
#     sum =  0
#     for i in range(length-2,-1,-2):
#       number = eval(num[i])
#       number = number * 2
#       if number > 9:
#           strNumber = str(number)
#           number = eval(strNumber[0]) + eval(strNumber[1])
#           sum += number
#       return sum


def sumOfDoubleEvenPlace(cardNumber):
    result = 0

    for i in range(len(cardNumber) - 2, -1, - 2):
        result += getDigit(int(cardNumber[i]) * 2)

    return result

cardNumber = '379307921301000'

result = 0

for i in range(len(cardNumber) -2 , -1, -2 ):
    print(cardNumber[i])

print(result)
# 4
# 3
# 8
# 8
# 5
# 0
-2
# 4
# 3
# 8
# 0


def getDigit(number):
    # print(number % 10, 'test')# 1
    # print(number // 10 % 10, 'limp')# 2
    return number % 10 + (number // 10 % 10)# 3
print(getDigit(21))
#3
print(getDigit(4))

print(sumOfDoubleEvenPlace('4388576018402626'))



# str = "this is string example....wow!!!";
# print str.startswith( 'this' )
# print str.startswith( 'is', 2, 4 )
# print str.startswith( 'this', 2, 4 )
# True
# True
# False

def isValid(CCNumber):
# Return true if the card number is valid
#hint you will have to call function sumOfDoubleEvenPlace() and sumOfOddPlace
    if ((CCNumber.startswith("4") or CCNumber.startswith("5") or
           CCNumber.startswith("6") or CCNumber.startswith("37")) and \
           (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0):
           return True
# str = "this is string example....wow!!!";
# print(str.startswith( 'this' ))
# True

isValid('4388576018402626')
