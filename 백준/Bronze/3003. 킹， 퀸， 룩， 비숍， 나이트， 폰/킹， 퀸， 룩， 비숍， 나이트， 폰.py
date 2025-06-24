chess = list(map(int, input().split()))
white = [1,1,2,2,2,8]
result = []

for i in range(len(chess)):
    print(white[i]-chess[i], end=" ")