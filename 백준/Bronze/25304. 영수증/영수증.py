import sys
buy = int(input())
N = int(input())
sum = 0

for i in range(N):
    A,B = map(int, sys.stdin.readline().split())
    sum += A*B

if(buy == sum):
    print("Yes")
else:
    print("No")