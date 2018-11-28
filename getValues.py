#Write a program to let user enter a list of number calculate the sum and average of the use of numbers

def get_values()->(list):#function to get values from user
    

    return value_list

def get_total(value_list): #function to calculate sum of number in list
    total = 0
    for num in value_list:
        total = total + num
    return total

def get_avg(total, length): #function to calculate average of the list of numbers
    return total/length

def main():
    numList = get_values()
    total = get.total(numList)
    length = len(numList)
    avg = get_avg(total, length)

if __name__=="__main__":
    main()
