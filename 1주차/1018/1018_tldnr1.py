import sys

def checking(arr, x, y):
    matrix = [arr[i][x:x+8] for i in range(y,y+8)]
    w_cnt = 0
    b_cnt = 0

    # 틀린 값 찾기
    for j in [0, 2, 4, 6]:
        for i in [0, 2, 4, 6]:
            if matrix[j][i] == 'W':
                b_cnt += 1
            elif matrix[j][i] == 'B':
                w_cnt += 1
        for i in [1, 3, 5, 7]:
            if matrix[j][i] == 'W':
                w_cnt += 1
            elif matrix[j][i] == 'B':
                b_cnt += 1
    for j in [1, 3, 5, 7]:
        for i in [0, 2, 4, 6]:
            if matrix[j][i] == 'W':
                w_cnt += 1
            elif matrix[j][i] == 'B':
                b_cnt += 1
        for i in [1, 3, 5, 7]:
            if matrix[j][i] == 'W':
                b_cnt += 1
            elif matrix[j][i] == 'B':
                w_cnt += 1

    return w_cnt if w_cnt <= b_cnt else b_cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]

min_cnt = 1e9
for j in range(n - 7):
    for i in range(m - 7):
        cnt = checking(board, i, j)
        if cnt < min_cnt:
            min_cnt = cnt

print(min_cnt)
