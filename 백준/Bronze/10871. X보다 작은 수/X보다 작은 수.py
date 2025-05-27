N,X = map(int, input().split())
numbers = []

numbers += list(map(int, input().split()))

for j in numbers:
    if(j < X):
        print(j, end=" ")