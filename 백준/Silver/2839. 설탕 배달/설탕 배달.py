# 2839
N = int(input())
result = 0

while N >= 0:  # 0 이상이어야 N=0 일때 N%5==0 조건 참
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break

    if 0 < N < 3:
        print(-1)
        break

    N -= 3
    result += 1
