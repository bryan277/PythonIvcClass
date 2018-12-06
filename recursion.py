# function that calls itself

# main -> a -> b -> c -> d
#non-recursive or iterative

# main -> a -> a -> a -> a
# recursive

# whenever possible use iterative over recursive, why?

# Example
def main():
    message()

def message():
    print("this is a recursive function")
    message()

main()


#There are 2 parts of a recursive definition (recurence relation)
# stopping case
# trivial case

# 4! = 4 * 3 * 2 * 1
# 3! = 3 * 2 * 1
# 2! = 2 * 1
# 1! = 1
# 0! = 1
#
# fact(n) = n * fact(n - 1)
# fact(4) = 4 * fact(3)
# fact(3) = 3 * fact(2)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def main():
    n = int(input("Enter < non-negative integer"))
    f = fact(n)
    print('The factorial of ', n, 'is', f)


main()

#recursive tree
# fact(4)
#     4 * fact(3)
#         3 * fact(2)
#             2 * fact(1)
#                 1 * fact(0)


#Find 2^n where n is a non-negative integer

# 2^3 = 2. 2.2
# 2^2 = 2.2
# 2^1 = 2
# 2^0 = 1

two(n) = 2 * two(n-1)
two(3) = 2 * two(2)
