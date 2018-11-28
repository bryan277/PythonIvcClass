#if-else Statments
temp = 35

if temp < 40:
    print('wear a jacket')
else:
    print('wear swim suit')

avg = 85
if avg >= 90 and avg <= 100:
    print('A')
elif avg >= 80 and avg <= 89:
    print('B')
elif avg >= 70 and avg <= 79:
    print('C')
elif avg <= 69:
    print('F')
else: #avg < 0 or avg > 100:
    print("out of range")
#B

avg = 110
if avg < 0 or avg > 100:
    print('Invalid')
else:
    if avg >= 90:
        print('A')
    else:
        if avg >= 80:
            print('B')
        else:
            if avg >= 70:
                print('C')
            else:
                if avg >= 60:
                    print('F')
#Invalid
#elif
avg = 45
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
