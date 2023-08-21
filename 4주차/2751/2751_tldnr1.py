import sys

n = int(sys.stdin.readline().rstrip())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

numbers.sort()
for i in numbers:
    print(i)