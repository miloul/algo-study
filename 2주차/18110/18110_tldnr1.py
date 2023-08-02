import sys


def new_round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)


n = int(sys.stdin.readline().rstrip())
if n:
    lv = []
    for _ in range(n):
        lv.append(int(sys.stdin.readline().rstrip()))

    lv.sort()
    percent = new_round(len(lv) * 0.15)

    if percent > 0:
        print(new_round(sum(lv[percent:-percent]) / len(lv[percent:-percent])))
    else:
        print(new_round(sum(lv) / len(lv)))
else:
    print(0)
