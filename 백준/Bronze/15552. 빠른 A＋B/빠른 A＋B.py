import sys

total = int(sys.stdin.readline())
for i in range(total):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)