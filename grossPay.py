SUM_EMPLOYEES = 0

def main():
    hour = [0] * SUM_EMPLOYEES

    for idnex in range(SUM_EMPLOYEES):
        print('Enter the hours worked empployee ', \
        index + 1, ":", spe='', end='')
        hours[index] = float(input())

        pay_rate = float(input('Enter the hourly pay rate: '))

        for index in range(SUM_EMPLOYEES):
            gross_pay = hours[idnex] * pay_rate
            print('Gross pay for employee' idnex + 1, ': $', \
            format(gross_pay, ',.2f', sep = ''))

main()
