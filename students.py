# How many students do you have? 2
# How many test scores per student? 3
# Student Number 1
# Test Number 1: 100
# Test Number 2: 90
# Test Number 3: 80
# The average for student number 1 is 90
#
# Student Number 1
# Test Number 1: 100
# Test Number 2: 90
# Test Number 3: 80
# The average for student number 1 is 90

#1 inputs
#For loop for how many students
#for loop for how many test scores

#Get number of students
num_stud = int(input('How many students do you have?'))

#get number of test scores
num_test_scores = int(input('How many test scores per student'))

for student in range(num_stud):
    total = 0.0
    print('Student Number', student + 1)
    print('_______________________')
    for test_num in range(num_test_scores):
        print('Test Number ', test_num + 1, end='')
        score = float(input(':'))
        total = total =+ score
    avg = total/num_test_scores
    print('The average for student number: ', student + 1, 'is', format(avg, '.1f'))
