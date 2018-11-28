#For how many days do you have sales?(5)
#Enter sales for day #1 10000.00
                     #2 20000.00
                     #3 30000.00
                     #4 40000.00
                     #5 50000.00


def main():
    num_days = int(input('For how many days do you have sales ?'))
    sales_file = open('sales.txt','w')
    for count in range(1, num_days + 1):
        sales = flaot(input('Enter the sales for day # ' + str(count) + ':'))
        sales_file.write(str(sales) + '\n')

    sales_file.close()
    print('Data wrtten to file')

main()

#read sales_txt file with checking of
