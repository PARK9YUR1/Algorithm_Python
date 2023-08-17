T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    mid = N // 2 + N % 2
    c1 = card[:mid]
    c2 = card[mid:]

    print(f'#{tc} ', end='')
    for i in range(mid):
        print(c1[i], end=' ')
        if N % 2 == 1 and i == mid - 1:
            continue
        print(c2[i], end=' ')
    print()