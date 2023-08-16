T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생들의 수
    box = [0] * 201
    for _ in range(N):
        S, E = map(int, input().split())
        if S > E:
            S, E = E, S
        S = S//2 + S%2
        E = E//2 + E%2
        for i in range(S, E+1):
            box[i] += 1

    result = max(box)
    print(f'#{tc} {result}')