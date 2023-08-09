import sys

n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
checks = list(map(int, sys.stdin.readline().rstrip().split()))

_dict = {}
for i in range(len(cards)):
    if cards[i] in _dict:
        _dict[cards[i]] += 1
    else:
        _dict[cards[i]] = 1

for check in checks:
    if check in _dict:
        print(_dict[check])
    else:
        print(0)
