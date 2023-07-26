num = int(input())

memo = [0, 0, 1, 1] + [0] * (num - 3)

if num <= 3:
    print(memo[num])
else:
    for i in range(4, num + 1):
        command = [0] * 3  # x3, x2, +1

        # x3
        if i % 3 == 0:
            command[0] = memo[i // 3] + 1
        else:
            command[0] = 1234567891

        # x2
        if i % 2 == 0:
            command[1] = memo[i // 2] + 1
        else:
            command[1] = 1234567891

        # +1
        command[2] = memo[i - 1] + 1

        memo[i] = min(command)

    print(memo[num])
