
#CS10
#1003181
#Homework 3 set 3
#Due exam 3

def main():
    #user will input the credit card number as a string
    CCNumber = str(input('Enter a credit card number as a long integer: '))
    #call the function isValid() and print whether the credit card number is valid or not valid
    if isValid(CCNumber):
        print(CCNumber + ' is valid')
    else:
        print(CCNumber + ' is not valid')

# Return true if the card number is valid
#Functions sumOfDoubleEvenPlace() and sumOfOddPlace() are called
def isValid(number):
    if ((number.startswith("4") or number.startswith("5") or number.startswith("6") or number.startswith("37")) and (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0):
        return True
# str = "this is string example....wow!!!";
# print(str.startswith('this'))
# True

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    result = 0

    for i in range(len(number) - 2, -1, - 2):#pulls every even number from number
        result += getDigit(int(number[i]) * 2)#getDigit function

    return result

#Returns number if it is a single digit, otherwise, return
#The sum of the two digits
def getDigit(number):
    return number % 10 + (number// 10 % 10)
# print(number % 10)# 1
# print(number // 10 % 10)# 2
# print(getDigit(2))
#2
# print(getDigit(21) * 2)
#6

def sumOfOddPlace(number):
# Return sum of odd place digits in number
    result = 0

    for i in range(len(number)-1, -1, -2):#pulls every odd number from number
        result += int(number[i])

    return result

if __name__=="__main__":
    main()#calls main function

#Output
# Enter a credit card number as a long integer: 4388576018402626
# 4388576018402626 is not valid
# Enter a credit card number as a long integer: 4388576018410707
# 4388576018410707 is valid
