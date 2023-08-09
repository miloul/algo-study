import sys

n = int(sys.stdin.readline().rstrip())
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
numbers.sort()

# 산술 평균
print(round(sum(numbers) / n))

# 중앙값
print(numbers[n//2])

# 최빈값
dic = dict()
for number in numbers:
    if number in dic:
        dic[number] += 1
    else:
        dic[number] = 1

mx = max(dic.values())  # 빈도수 최댓값
mx_dic = []

for i in dic:
    if mx == dic[i]:  # 빈도수 최댓값 key 저장
        mx_dic.append(i)

if len(mx_dic)>1:
    print(mx_dic[1])   # 최빈값 2개 이상인 경우 2번째 출력
else:
    print(mx_dic[0])

# 범위
print(numbers[-1] - numbers[0])
