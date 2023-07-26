from math import factorial

n = int(input())
factorial_n = str(factorial(n))[::-1]

for i in range(len(factorial_n)):
    if factorial_n[i] != '0':
        print(i)
        break