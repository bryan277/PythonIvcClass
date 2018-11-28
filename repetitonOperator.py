list * n
num = [0] * 5
print(num)
# [0, 0, 0, 0, 0]

num = [1,2,3] * 3
print(num)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

num = [99, 100, 101, 102]

for n in num:
    print(n)
# 99
# 100
# 101
# 102

#Accessing list with index
list = [10, 20, 30, 40]
print(list[0,], list[1], list[2], list[3])


#or

index = 0
while index < 4:
    print(list[index])
    index = index + 1

#The len() function
list = [1,2,3,4]
size = len(list)
print(size)
#4

list = [10, 20 , 30, 40]
index = 0
while index < len(list):
    print(list[index])
    index += 1
# 10
# 20
# 30
# 40

num = [1,2,3,4,5]
print(num)
# [1, 2, 3, 4, 5]

num[0] = 99
print(num)
# [99, 2, 3, 4, 5]

#Fill a list with value using index
#1.create a list
#2.fill the list

#create list of 5 elements
num = [0] * 5
#fill the list
index = 0
while index < len(num):
    num[index] = 99
    index += 1

print(num)
# [99, 99, 99, 99, 99]

#Enter sales for each Day
#Day 1 100001
#Day 2 100002

ndays = 5

def main():
    #create list1
    sales = [0] *ndays
    #get sales data
    print('Enter sales for each day')

index = 0
while index < ndays: #index<len(sales)
    print('Day #', index + 1, ':b', start= '', end= '')
    sales[index] = float(input())
    index += 1

#display
print('Here are the value you entered')
for value in sales:
    print(value)

#Concatenating lists
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = ['Jimmy', 'Jones']
list4 = list1 + list2
