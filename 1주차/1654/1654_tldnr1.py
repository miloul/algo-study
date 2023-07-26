import sys

k, n = map(int, sys.stdin.readline().split())
lan_cable = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

lt = 1
rt = sum(lan_cable)//n
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for cable in lan_cable:
        cnt += cable // mid

    if cnt >= n:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)