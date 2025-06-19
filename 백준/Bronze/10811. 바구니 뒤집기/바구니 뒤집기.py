N, M = map(int, input().split())
num =[i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = num[i-1:j]
    temp.reverse()
    num[i-1:j] = temp
    
for i in num:
    print(i, end=" ")