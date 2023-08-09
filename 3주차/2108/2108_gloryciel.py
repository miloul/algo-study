import sys
from collections import Counter

def round_half_up(a):
    if(a>=0):
        if(a-int(a)>=0.5):
            return int(a)+1
        else:
            return int(a)
    else:
        a=abs(a)
        if (a >= 0):
            if (a - int(a) >= 0.5):
                return -(int(a) + 1)
            else:
                return -(int(a))

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
counter = Counter(numbers)

print(round_half_up(sum(numbers)/N))
print(numbers[N//2])
if(N>=2):
    if(counter.most_common(2)[0][1]==counter.most_common(2)[1][1]):
        print(counter.most_common(2)[1][0])
    else:
        print(counter.most_common(2)[0][0])
else:
    print(numbers[0])
print(max(numbers)-min(numbers))
