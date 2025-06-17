std = [0] * 31

for i in range(28):
    num = int(input())
    std[num] = 1
    
for i in range(1, 31):
    if(std[i] == 0):
        print(i)