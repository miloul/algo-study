words = []
for _ in range(int(input())):
    words.append(str(input()))

words = list(set(words))
words.sort()
words.sort(key = len)

for word in words:
    print(word)
