from collections import deque

n = int(input())

deq = deque()
for i in range(1, n+1):
    deq.append(i)

while len(deq) > 1:
    deq.popleft()
    rotate_num = deq.popleft()
    deq.append(rotate_num)

print(deq[0])
