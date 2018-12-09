#Hans Vos
#1003181
#Due final exam
#hw5 set #3


class Loan:

    def __init__(self):
        self.__annualRate = float()
        self.__yearsLoan = float()
        self.__loanAmount = float()
        self.__name = str()

    # Setters
    def setAnnualRate(self):
        annualInterestRate = float(input('Enter yearly interest rate, for example, 7.25: '))
        annualInterestRate = annualInterestRate / 100
        self.annualRate = annualInterestRate

    def setYearsLoan(self):
        yearsLoan = float(input('Enter number of years as an integer: '))
        self.yearsLoan = yearsLoan

    def setLoanAmount(self):
        loan = float(input('Enter loan amount, for example, 120000.95: $'))
        self.loanAmount = loan

    def setName(self):
        name = input("Enter a borrowers's name: ")
        self.name = name

    #Getter
    def getAnnualRate(self):
        return self.annualRate

    def getYearsLoan(self):
        return self.loanAmount

    def getName(self):
        return self.name

    def getMonthlyPayment(self):
        monthlyInterestRate = self.annualRate / 12
        monthlyPayment = self.loanAmount * monthlyInterestRate / (1 - (1 / (1 +monthlyInterestRate) ** (self.yearsLoan * 12)))
        return monthlyPayment

    def getTotalPayment(self):
        monthlyPayment = float(self.getMonthlyPayment())
        totalPayment = monthlyPayment * self.yearsLoan * 12
        return totalPayment

def main():
    loan = Loan()
    loan.setAnnualRate()
    loan.setYearsLoan()
    loan.setLoanAmount()
    loan.setName()
    print('The loan is for', loan.name)
    print('The monthly payment is $', format(loan.getMonthlyPayment(), ',.2f'))
    print('The total payment is $', format(loan.getTotalPayment(), ',.2f'))
    print()
    repeat = input('Do you want to change the loan amount? Enter "Y" for yes, press enter to quit: ')
    while repeat.upper() == 'Y':
        loan.loanAmount = float(input('Enter new loan amount: $'))
        print('The loan is for', loan.name)
        print('The monthly payment is $', format(loan.getMonthlyPayment(), ',.2f'))
        print('The total payment is $', format(loan.getTotalPayment(), ',.2f'))
        print()
        again = input('Do you want to change the loan amount? Enter "Y" for yes, press enter to quit: ')

main()

# Enter yearly interest rate, for example, 7.25: 2.5
# Enter number of years as an integer: 5
# Enter loan amount, for example, 120000.95: $1000.00
# Enter a borrowers's name: John Jones
# The loan is for John Jones
# The monthly payment is $ 17.75
# The total payment is $ 1,064.84
#
# Do you want to change the loan amount? Enter "Y" for yes, press enter to quit: Y
# Enter new loan amount: $5000
# The loan is for John Jones
# The monthly payment is $ 88.74
# The total payment is $ 5,324.21
