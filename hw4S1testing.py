ONE_TEN = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def hasAdjacentDuplicate(arr):
#     return any([i==j for (i, j) in zip(arr, arr[1:])])#any() returns:
#                                                       # True if at least one element of an iterable is true
#                                                       # False if all elements are false or if an iterable is empty
#
# def my_sort(numbers):
#     odd  = [n for n in numbers if n % 2 != 0]
#     even = [n for n in numbers if n % 2 == 0]
#     return sorted(even) + sorted(odd)
#
# print(my_sort(ONE_TEN))

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[:2] + numbers[3:])
# print(numbers.pop((len(numbers)-1)//2)
#
#
#
# aList = [1,2,3,4,5]
# #minus 1 because the first element is index 0
# middleIndex = (len(aList) - 1)/2
# print(middleIndex)
# print(aList[middleIndex])
# def Remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             return True
#         else:
#             return False
#
# # Driver Code
# duplicate1 = [1,2,3,4,5,6]
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))
# print(Remove(dup))
# a = [3,6,2,67,4,8,9,32,12,12]
#
# print(a.pop(1))
# #2
# print(len(a))
# #12
# print(len(a) - 1)
# #11
# print(11//2)
# #5
# print(a.pop(5))
# #8
# print(a.pop((len(a)-1)//2))

your_list = [1,2,3,4,5]
# print(len(your_list) != len(set(your_list)))
#
# def hasDuplicate(arr):
#     return len(arr) != len(set(arr))


print(len(your_list))
#3
print(len(set(your_list)))
#2
print(hasDuplicate(your_list))
