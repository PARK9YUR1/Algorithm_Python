T = int(input())
for tc in range(1, T+1):
    # 손님 N명, M초 동안 K개 붕어빵
    N, M, K = map(int, input().split())
    sn = list(map(int, input().split()))
    sn.sort()

    if sn[0] < M:
        print(f'#{tc} Impossible')
        continue

    result = 'Possible'
    time = bread = cnt = 0

    while True:
        time += 1
        if time % M == 0:
            bread += K

        for s in sn:
            if s == time and bread > 0:
                bread -= 1
                cnt += 1
            elif s == time and bread <= 0:
                result = 'Impossible'

        if result == 'Impossible' or cnt == N:
            break

    print(f'#{tc} {result}')