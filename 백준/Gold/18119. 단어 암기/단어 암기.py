import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = [0 for _ in range(N)]

alpha_check = (1 << 26) - 1

for i in range(N):
    word = set(input().rstrip())
    for w in word:
        x = ord(w) - 97
        check[i] = check[i] | (1 << x)

for _ in range(M):
    num, alpha = input().split()
    x = ord(alpha) - 97

    if num == '1':  # alpha를 잊는다 : 1 -> 0
        bit = (alpha_check >> x) & 1
        if bit== 1:
            alpha_check = alpha_check ^ (1 << x)

    else: # num == '2' -> alpha를 기억해낸다. : 0 -> 1
        alpha_check = alpha_check | (1 << x)

    cnt = 0
    for i in range(N):
        if alpha_check & check[i] == check[i]:
            cnt += 1
    print(cnt)