num = []

for _ in range(10):
    num.append(int(input()) % 42)

count_num = list(set(num))
print(len(count_num))