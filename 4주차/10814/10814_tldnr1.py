n = int(input())
arr = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age, name))

members = sorted(arr, key=lambda x: x[0])
for member in members:
    print(member[0], member[1])