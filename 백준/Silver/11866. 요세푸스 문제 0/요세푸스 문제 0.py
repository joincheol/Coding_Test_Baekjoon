N, K = map(int, input().split())
num = []
index = 0
result = []

for i in range(1, N+1):
    num.append(i)

while len(num):
    index = (index + K - 1) % len(num)
    result.append(num.pop(index))

print('<' + ', '.join(map(str, result)) + '>')
