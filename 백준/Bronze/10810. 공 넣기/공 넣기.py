N, M = map(int, input().split())
basket = []
for _ in range(N):
    basket.append(0)

for _ in range(M):
    i,j,k = map(int, input().split())
    for ball in range(i,j+1):
        basket[ball-1]=k

for status in basket:
    print(status, end=" ")