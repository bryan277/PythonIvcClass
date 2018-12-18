#Hans Vos
#1003181
#Dec 10

from tkinter import *

window = Tk() #Creates window
window.title("Loan calculator") #Sets the window title

Label(window, text="Annual Interest Rate:").grid(row=0) #creates the label and grid is alignment
Label(window, text="Number of Years:").grid(row=1) #label for years
Label(window, text="Loan Amount:").grid(row=2) #label for loan amount
Label(window, text="Monthly Payment:").grid(row=3)
Label(window, text="Total Payment:").grid(row=4)

#Entry1
entry1 = Entry(window, justify=RIGHT) #it creates text box to enter details
entry1.grid(row=0, column= 1)
#Entry2
entry2 = Entry(window, justify=RIGHT)
entry2.grid(row=1, column=1)
#Entry3
entry3 = Entry(window, justify=RIGHT)
entry3.grid(row=2, column=1)

def calc():
    annualInterestRate = float(entry1.get())  #gets the values in text boxes into the varibles
    time = float(entry2.get())
    loanAmount = float(entry3.get())
    monthlyInterestRate = annualInterestRate/1200
    monthlyPayment = loanAmount * monthlyInterestRate/(1-(1/(1+monthlyInterestRate)**(time * 12))) #formula shown in above program
    totalPayment = monthlyPayment * time * 12 #calculates the total payment
    output1 = str(round(monthlyPayment, 2))
    output2 = str(round(totalPayment, 2))
    labal_mp = Label(window, text = output1).grid(row = 3, column=1, sticky= E) # creates two new labels to print details
    label_tp = Label(window, text = output2).grid(row = 4, column=1, sticky= E)
    return

Button(window, text='Compute Payment', command=calc).grid(row = 5, column = 1, sticky = W, pady = 4)

mainloop()
