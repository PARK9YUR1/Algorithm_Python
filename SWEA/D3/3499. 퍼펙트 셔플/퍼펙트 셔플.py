T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    mid = N // 2 + N % 2
    c1 = card[:mid]
    c2 = card[mid:]

    new_card = []
    for i in range(mid):
        new_card.append(c1[i])
        if N % 2 == 1 and i == mid - 1:
            continue
        new_card.append(c2[i])

    print(f'#{tc}', *new_card)