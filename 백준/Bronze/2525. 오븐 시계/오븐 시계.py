H, M = map(int, input().split())
T = int(input())

total = H * 60 + M + T
H = (total // 60) % 24
M = total % 60

print(H, M)