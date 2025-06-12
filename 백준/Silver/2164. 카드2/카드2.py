from collections import deque

N = int(input())
card = deque()

for i in range(1, N+1):
    card.append(i)

while(True):
    if(len(card) == 1):
        break
    card.popleft()
    temp = card[0]
    card.popleft()
    card.append(temp)

print(card[0])