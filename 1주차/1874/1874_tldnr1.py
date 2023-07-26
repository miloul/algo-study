import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
numbers = deque(int(sys.stdin.readline().rstrip()) for _ in range(n))
ascending = [0]
i = 1

command = []
while numbers:
    if ascending[-1] == numbers[0]:
        command += '-'
        ascending.pop()
        numbers.popleft()
    elif ascending[-1] < numbers[0]:
        if i <= numbers[0]:
            command += '+'
            ascending.append(i)
            i += 1
        else:
            command += 'x'
            break
    else:
        command += 'x'
        break

if command[-1] == 'x':
    print('NO')
else:
    for c in command:
        print(c)