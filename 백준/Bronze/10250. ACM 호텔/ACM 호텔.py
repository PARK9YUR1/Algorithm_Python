import sys
input = sys.stdin.readline

T = int(input())  # 테스트데이터
for _ in range(T):
    H, W, N = map(int, input().split())  # 호텔층수, 방수, N번째손님
    hotel = [['']*W for _ in range(H)]
    num = [['']*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            hotel[h][w] = str(H-h) + str('%02d'%(w+1))

    n = 1
    for w in range(W):
        for h in range(H-1, -1, -1):
            num[h][w] = n
            n += 1

    for h in range(H):
        for w in range(W):
            if N == num[h][w]:
                print(hotel[h][w])
                break