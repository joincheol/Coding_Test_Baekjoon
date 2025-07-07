import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

def push(num):
    stack.append(num)

def pop():
    if(len(stack) >= 1):
        print(stack.popleft())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if(len(stack) == 0):
        print(1)
    else:
        print(0)

def front():
    if(len(stack) >= 1):
        print(stack[0])
    else:
        print(-1)

def back():
    if(len(stack) >= 1):
        print(stack[-1])
    else:
        print(-1)

for i in range(N):
    order = sys.stdin.readline().split()
    if(order[0] == 'push'):
        num = int(order[1])
        push(num)
    elif(order[0] == 'pop'):
        pop()
    elif(order[0] == 'size'):
        size()
    elif(order[0] == 'empty'):
        empty()
    elif(order[0] == 'front'):
        front()
    elif(order[0] == 'back'):
        back()