n, m = map(int, input().split())
ns = list(map(int, input().split()))
ns.sort()

def ink(a, b):
    return 5 + 2 * (b - a + 1)

need = []
for i in range(1, n + 1):
    if i not in ns:
        need.append(i)

mink = 0
if need:
    st = need[0]

    for i in range(len(need)):
        if i + 1 < len(need):
            if need[i + 1] - need[i] > 3:
                mink += ink(st, need[i])
                st = need[i + 1]
            else:
                continue
        else:
            mink += ink(st, need[i])

print(mink)
