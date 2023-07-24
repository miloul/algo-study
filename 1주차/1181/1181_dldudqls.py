def lenSort(w):
    n = len(w)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(w[j]) > len(w[j+1]):
                w[j], w[j+1] = w[j+1], w[j]


n = int(input())
words = [input().strip() for _ in range(n)]
words.sort()
lenSort(words)
a = []
for t in words:
    if t not in a:
        a.append(t)
for i in a:
    print(i)