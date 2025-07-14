line = []

for i in range(9):
    line.append(int(input()))

total = sum(line)

for i in range(9):
    for j in range(i+1, 9):
        if(total - line[i] - line[j] == 100):
            num1 = line[i]
            num2 = line[j]
            break

line.remove(num1)
line.remove(num2)
line.sort()

for i in line:
    print(i)