T = int(input())
for tc in range(1, T+1):
    lst = [0] * 201
    N = int(input())  # 돌아가야 할 학생 수
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        for i in range((a+1)//2, (b+1)//2+1):
            lst[i] += 1

    result = max(lst)
    print(f'#{tc} {result}')