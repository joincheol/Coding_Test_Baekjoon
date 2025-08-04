N = int(input())
result = list(input())

for i in range(N-1):
    temp = list(input())
    for j in range(len(result)):
        if(result[j] != temp[j]):
            result[j] = '?'

print(''.join(result))