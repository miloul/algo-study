import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())

# sum(list, []) => 2차원 list 를 1차원 으로 바꿔줌
blocks_list = sum([list(map(int, sys.stdin.readline().split())) for _ in range(n)], [])
blocks = Counter(blocks_list)

bottom = min(blocks)
top = max(blocks)

res_time = 1234567891
res_height = 0

# blocks 의 min, max 외의 높이는 정답이 될 수 없음
for height in range(bottom, top + 1):
    use_block = 0
    take_block = 0

    # blocks[block] => block 높이 몇 개?
    for block in blocks:
        if block > height:
            take_block += blocks[block] * (block - height) # 튀어나온 높이
        else:
            use_block += blocks[block] * (height - block)  # 들어간 높이

    if use_block > take_block + b:
        continue

    time = take_block * 2 + use_block
    # print(height, ':', use_block, take_block, time)

    if time <= res_time:
        res_time = time
        res_height = height

print(res_time, res_height)
