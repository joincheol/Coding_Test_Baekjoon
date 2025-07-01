import sys

N = int(input())
order = []

for _ in range(N):
    order.append(int(sys.stdin.readline()))

order.sort()

for i in order:
    print(i)