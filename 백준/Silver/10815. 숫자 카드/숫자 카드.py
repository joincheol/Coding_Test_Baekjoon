N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

result = {}

for i in card1:
    result[i] = True

for i in card2:
    if(i in result):
        print("1", end=" ")
    else:
        print("0", end=" ")