import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque(list(range(1,N+1)))

while len(arr)!=1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])
