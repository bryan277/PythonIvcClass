#Records
# A record is a complete se of data about an item, and a field is an individual peice of data within a record
# save employee recrods to file

def main():
    num_emps = int(input('How many employee recrods do you want?'))
    emp_file = open('employees.txt', 'w')
    for count in range(1, num_emps):
        print('Enter data for Employee #', count, sep = '')
        name = input('Name:')
        id_num = input('ID:')
        dept = input('Department:')
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
    emp_file.close()
    print('Data written file')

main()
