num = []

for i in range(9):
    num.append(list(map(int, input().split())))

max_num = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if(max_num <= num[i][j]):
            max_num = num[i][j]
            row = i+1
            col = j+1

print(max_num)
print(row, col)