text = input().upper()
alpha = list(set(text))
cnt = []

for i in alpha:
    cnt.append(text.count(i))

if(cnt.count(max(cnt)) > 1):
    print("?")
else:
    print(alpha[cnt.index(max(cnt))])