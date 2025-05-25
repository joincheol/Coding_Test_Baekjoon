import sys
info = []

N = int(input())
for i in range(N):
    w, h = map(int, sys.stdin.readline().split())
    info.append([w,h])

for j in info:
    order = 1
    for k in info:
        if(j[0] < k[0] and j[1] < k[1]):
            order += 1
    print(order, end=" ")