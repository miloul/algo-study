import sys
from collections import deque

I = [-1, 1, 0, 0]
J = [0, 0, -1, 1]

def chk(warehouse,i,j,N,M):
    if i<0 or i>=N:
        return False
    if j<0 or j>=M:
        return False
    if warehouse[i][j]==-1:
        return False
    return True

def BFS(warehouse,tomato,N,M):
    while tomato:
        now = tomato.popleft()
        for x in range (4):
            if chk(warehouse,now[0]+I[x],now[1]+J[x],N,M):
                if warehouse[now[0]+I[x]][now[1]+J[x]]==0:
                    tomato.append([now[0]+I[x],now[1]+J[x]])
                    warehouse[now[0] + I[x]][now[1] + J[x]]=warehouse[now[0]][now[1]]+1


M,N = map(int,sys.stdin.readline().split())
warehouse = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tomato = deque([])

for i in range (N):
    for j in range(M):
        if warehouse[i][j]==1:
            tomato.append([i,j])

BFS(warehouse, tomato, N, M)

day = 0
for i in range(N):
    for j in range(M):
        if(warehouse[i][j]==0):
            print(-1)
            exit(0)
        if(day<warehouse[i][j]):
            day = warehouse[i][j]
print(day-1)
