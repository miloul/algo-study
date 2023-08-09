n, m = map(int, input().split())
pages = set(i for i in range(1, n+1))

# 바닥의 논문 제거
trash_page = set(map(int, input().split()))
to_print = sorted(list(pages - trash_page))

ink = 0
if to_print:
    # A to B를 출력할 때, A를 target
    target = to_print[0]
    # (0,1) ~ (n-1,n)까지 탐색
    for i in range(len(to_print)-1):
        # 5+2*4 > (5+2)*2 == 연속 복사가 손해
        if to_print[i+1] - to_print[i] >= 4:
            # 사용한 잉크 계산
            ink += 5 + 2 * (to_print[i] - target + 1)
            target = to_print[i + 1]
    # 마지막 부분 더하기 (마지막에 연속된 장을 뽑아야 하는 경우)
    ink += 5 + 2 * (to_print[-1] - target + 1)
    print(ink)
else:
    print(0)
