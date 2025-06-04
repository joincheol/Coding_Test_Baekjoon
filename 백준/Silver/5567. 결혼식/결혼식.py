n = int(input())
m = int(input())

friends = [[] for i in range(n + 1)]

for j in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

invited = set()

for k in friends[1]:
    invited.add(k)
    for ftf in friends[k]:
        if ftf != 1:
            invited.add(ftf)

print(len(invited))