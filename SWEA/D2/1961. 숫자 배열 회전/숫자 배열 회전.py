T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = [list(map(str, input().split())) for _ in range(N)]

    box90 = []
    box180 = []
    box270 = []

    for j in range(N):
        for i in range(N):
            box90.append(box[N-1 - i][j])
            box180.append(box[N-1 - j][N-1 - i])
            box270.append(box[i][N-1 - j])

    print(f'#{tc}')
    for i in range(0, N**2, N):
            print(''.join(box90[i:i+N]), ''.join(box180[i:i+N]), ''.join(box270[i:i+N]))