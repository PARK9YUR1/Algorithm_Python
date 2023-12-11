# 2839
N = int(input())
result = 0

while N:
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break

    if N < 5 and N % 3 == 0:
        result += 1
        print(result)
        break

    if 0 < N < 3:
        print(-1)
        break

    N -= 3
    result += 1


