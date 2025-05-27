import sys

N,X = map(int, sys.stdin.readline().split())
numbers = []

for i in range(N):
    numbers += list(map(int, sys.stdin.readline().split()))

for j in numbers:
    if(j < X):
        print(j, end=" ")