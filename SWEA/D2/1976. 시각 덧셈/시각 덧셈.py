T = int(input())
for i in range(1, T+1):
    time = list(map(int, input().split()))
    hour = (time[0] + time[2])%12
    minute = (time[1] + time[3])
    if(minute>=60):
        hour += 1
    minute %= 60
    print(f"#{i} {hour} {minute}")