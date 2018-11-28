
#CS10
#1003181
#Homework 3 set 2
#Due exam 3

#Palindrome function
def isPalindrome(word):
    if word[::-1] == word:#print('string'[::-1]) -> gnirts
        return True
    else:
        return False
# print(isPalindrome('mom'))
#True

#Main() function
def main():
    word = str(input('Enter a String : '))
    if word == '-1':#quits program when -1 is entered
        print('Program quits')
    else:
        if isPalindrome(word):
            print(word + ' is palindrome')
        else:
            print(word + ' is not palindrome')

if __name__=="__main__": 
    main()#calls main function

#Output
# Enter a String : print
# print is not palindrome
# Enter a String : mom
# mom is palindrome
# Enter a String : racecar
# racecar is palindrome
# Enter a String : -1
# Program quits
