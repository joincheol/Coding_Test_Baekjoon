T = int(input())
for i in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    print(f"#{i} {max(num) - min(num)}")