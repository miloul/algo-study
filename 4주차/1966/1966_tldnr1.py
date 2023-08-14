import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    _input = sys.stdin.readline().split()
    rank = deque((int(_input[i]), i) for i in range(n))

    cnt = 0
    while rank:
        if rank[0][0] != max(rank)[0]:
            first = rank.popleft()
            rank.append(first)
        else:
            out = rank.popleft()
            cnt += 1
            if out[1] == m:
                print(cnt)
                break
