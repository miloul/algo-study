n = int(input())
A = set(map(int, input().split()))
m = int(input())
num_set = list(map(int, input().split()))

for num in num_set:
    print(1) if num in A else print(0)