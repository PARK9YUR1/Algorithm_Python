T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(str, input())) for _ in range(N)]
    box2 = [b[::-1] for b in box]

    lst1 = ['']*(2*N-1)
    lst2 = ['']*(2*N-1)
    txt1 = txt2 = ''

    result = 'NO'
    for i in range(N):
        for j in range(N):
            # 1
            txt1 += box[i][j]
            if j == N - 1:
                txt1 += '.'

            # 2
            txt2 += box[j][i]
            if j == N - 1:
                txt2 += '.'

            # 3
            lst1[i+j] += box[i][j]

            # 4
            lst2[i+j] += box2[i][j]

    if 'ooooo' in txt1 or 'ooooo' in txt2:
        result = 'YES'

    for l in range(2*N-1):
        if 'ooooo' in lst1[l] or 'ooooo' in lst2[l]:
            result = 'YES'

    print(f'#{tc} {result}')