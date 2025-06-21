N = int(input())
num = []

for i in range(N):
    [x,y] = map(int, input().split())
    num.append([x,y])

num.sort(key = lambda x: (x[0], x[1]))
for i in num:
    print(i[0], i[1])