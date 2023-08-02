import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    test = sys.stdin.readline().rstrip()
    cnt = 0

    for t in test:
        if t == '(':
            cnt += 1
        elif t == ')':
            cnt -= 1

        if cnt < 0:
            break

    if cnt == 0:
        print("YES")
    else:
        print("NO")
