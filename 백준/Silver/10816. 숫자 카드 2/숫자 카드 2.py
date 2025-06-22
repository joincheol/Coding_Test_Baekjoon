import sys

N = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))

score = {}
for i in card1:
    if i in score:
        score[i] += 1
    else:
        score[i] = 1

for i in card2:
    if i in score:
        print(score[i], end=" ")
    else:
        print(0, end=" ")