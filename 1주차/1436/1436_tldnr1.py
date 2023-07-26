n = int(input())

x = 666
cnt = 0
while True:
    if str(x).count('666') >= 1:
        cnt += 1
        if cnt == n:
            print(x)
            break

    x += 1
