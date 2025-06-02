N = input()
num = []
for i in range(len(N)):
    num.append(int(N[i]))

num.sort(reverse=True)

for j in num:
    print(j, end="")