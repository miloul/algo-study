def decimal(num):
    if num == 1:
        return -1
    elif num == 2:
        return 1
    elif num % 2 == 0:
        return -1
    else:
        for i in range(3,int(num**0.5) + 1, 2):
            if num % i == 0:
                return -1
        return 1


m, n = map(int, input().split())

for i in range(m, n+1):
    if decimal(i) == 1:
        print(i)
