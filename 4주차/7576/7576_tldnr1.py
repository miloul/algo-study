import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]


def find_x(x):  # -1, 0, 1
    res = []
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == x:
                res.append((i, j, 0))
    return res


def multi_bfs(graph, start):
    queue = deque(start)
    days = 0
    while queue:
        x, y, day = queue.popleft()
        days = day
        # 상, 하, 좌, 우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 주변 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 밖 무시
                continue
            # -1 혹은 1 무시
            if graph[nx][ny] == 0:
                queue.append((nx, ny, day+1))
                graph[nx][ny] = 1
    return days


# 덜 익은 토마토 존재
if find_x(0):
    days = multi_bfs(tomato, find_x(1))
    # 다 익었는지 확인
    if find_x(0):
        print(-1)
    else:
        print(days)
else:
    print(0)