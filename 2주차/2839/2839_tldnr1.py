n = int(input())

cnt = 0
flag = 0
for y in range(n//5, -1, -1):
    for x in range(0, n//3 + 1):
        if 5*y + 3*x == n:
            print(y+x)
            flag = 1
            break
    if flag == 1:
        break
if flag == 0:
    print(-1)