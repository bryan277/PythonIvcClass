def main():
    numbers = [1,2,3,4,5]
    outfile = open('numbers1.txt', 'w')
    outfile.writelines(numbers)
    for item in numbers:
        outfile.write(item + '\n')
    outfile.close()

main()


# cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
# outfile = open('cities.txt', 'w')
# outfile.writelines(cities)
# outfile.close()

# def main():
#     cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
#     outfile = open('cities.txt', 'w')
#     for item in cities:
#         outfile.write(item + '\n')
#     outfile.close()

#
# def main():
#     num_days = int(input('For how many days do you have sales ?'))
#     sales_file = open('sales.txt','w')
#     for count in range(1, num_days + 1):
#         sales = flaot(input('Enter the sales for day # ' + str(count) + ':'))
#         sales_file.write(str(sales) + '\n')
#
#     sales_file.close()
#     print('Data wrtten to file')
