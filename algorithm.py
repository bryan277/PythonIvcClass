# algorithm - a deteced sequence of steps for carrying out some process. A receipe.

            # - Time always more than one algorithm to the same problem
            # - computer scientist study algorithm and came up with wasy to complete them and style which one better than others
            # - The most common criterion to compare algorithm is time(step)
            # - measure magnitude fo running time of algorithm
            # - the idea of big o is the express how much slower the program as input data get large
            # - focuses on steps to be excuted
            # - ignores - differences in language compiled vs interpreted

# loops - loops are multiplieactive in terms of time
#         nested loops multiply the n amount of time need to run the body, so its longerr time.


# sorting algorithm - sort data alphebetically or numerically in order
                    # ex. Bubblesort has complexity of
                    #     - you loops through elements in list
                    #     - compare a adjacent elements
                    #     - swap values if set of order


# To sort a if element list need 9 steps

# Bubblesort is efficient
# Quicksort - smarter, has complexity of (nlog(n))

# Searching - linear search - search through every single element in list sequentially
# worse case      end of list (n)
# average case    n/2
# best case       first element

# linear search is inefficient

# if we have a long list then linear search is inefficient, use Binary search 0(log(n))
# 1. the list sorted
# 2. half the list, compare the middle for a match
# 3. no match is middle index value greater or less than the keys
# 4. go the left or right and continue to half

# test

def bubblesort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if (lst[i] > lst[j]):
                t = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = t
    return lst


def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high)/2
        if key < lst[mid]
            high = mid -1
        elif key == lst[mid]
            return 'found'
        else:
            low = mid + 1
    return 'not found'

def main():
    lst + 1 = [11, 4, 7, 10, 2, 45, 50, 79, 60, 66, 69, 70, 59]
    lst = bubblesort(lst+ 1)
    print(lst)
    print(binarySearch(lst, 11))

main()
