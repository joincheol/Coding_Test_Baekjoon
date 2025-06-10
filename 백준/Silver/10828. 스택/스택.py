import sys

N = int(input())
num = []

for i in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == 'push'):
        num.append(order[1])
    elif(order[0] == 'pop'):
        if(len(num) >= 1):
            print(num.pop())
        else:
            print(-1)
    elif(order[0] == 'size'):
        print(len(num))
    elif(order[0] == 'empty'):
        if(len(num) == 0):
            print(1)
        else:
            print(0)
    elif(order[0] == 'top'):
        if(len(num) >= 1):
            print(num[-1])
        else:
            print(-1)