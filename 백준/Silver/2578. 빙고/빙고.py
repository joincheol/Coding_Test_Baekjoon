import sys

arr = []
for _ in range(5):
    arr.append(sys.stdin.readline().split())

num = []
for _ in range(5):
    list = sys.stdin.readline().split()
    for i in list:
        num.append(i)

check_board = [[False for _ in range(5)] for _ in range(5)]

def check_row_bingo():
    count = 0
    for i in range(5):
        is_bingo = True
        for j in range(5):
            if not check_board[i][j]:
                is_bingo = False
                break
        if is_bingo:
            count += 1
    return count

def check_column_bingo():
    count = 0
    for j in range(5):
        is_bingo = True
        for i in range(5):
            if not check_board[i][j]:
                is_bingo = False
                break
        if is_bingo:
            count += 1
    return count

def check_diagonal_bingo():
    count = 0
    is_bingo = True
    for i in range(5):
        if not check_board[i][i]:
            is_bingo = False
            break;
    if is_bingo:
        count += 1

    is_bingo = True
    for i in range(5):
        if not check_board[i][4 - i]:
            is_bingo = False
            break
    if is_bingo:
        count += 1
    return count

for i in range(25):
    now_num = num[i]
    for x in range(5):
        for y in range(5):
            if arr[x][y] == now_num:
                check_board[x][y] = True
    count = check_row_bingo() + check_column_bingo() + check_diagonal_bingo()
    if count >= 3:
        print(i+1)
        break