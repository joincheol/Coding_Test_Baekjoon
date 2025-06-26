import sys
sum = 0
avg = 0
total = 0

for i in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    credit = float(credit)
    if(grade == 'A+'):
        sum += credit * 4.5
        total += credit
    elif(grade == 'A0'):
        sum += credit * 4.0
        total += credit
    elif(grade == 'B+'):
        sum += credit * 3.5
        total += credit
    elif(grade == 'B0'):
        sum += credit * 3.0
        total += credit
    elif(grade == 'C+'):
        sum += credit * 2.5
        total += credit
    elif(grade == 'C0'):
        sum += credit * 2.0
        total += credit
    elif(grade == 'D+'):
        sum += credit * 1.5
        total += credit
    elif(grade == 'D0'):
        sum += credit * 1.0
        total += credit
    elif(grade == 'F'):
        sum += credit * 0
        total += credit
    elif(grade == 'P'):
        pass
avg = sum / total
print('%.6f' %avg)