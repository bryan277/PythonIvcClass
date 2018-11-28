sales = int(input('What are the sales?'))
if sales > 400:
    print('You met your sales quota')
else:
    print('You did not met the quota')


test1 = int(input('Enter test 1'))
test2 = int(input('Enter test 2'))
test3 = int(input('Enter test 3'))

avg = (test1 + test2 + test3)/3

if avg < 0 or avg > 100:
    print('invalid')
elif avg >= 90:
    print('A')
elif avg >= 80:
    print('B')
elif avg >= 70:
    print('C')
else:
    print('F')
