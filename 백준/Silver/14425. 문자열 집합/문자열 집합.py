N, M = map(int, input().split())
S = {}
count = 0

for i in range(N):
    S[input()] = 1

for i in range(M):
    if(input() in S):
        count += 1

print(count)