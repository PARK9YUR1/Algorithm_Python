T = int(input())
for _ in range(T):
    alpha, num = input().split('-')
    num = int(num)
    N = len(alpha)

    ans = 0
    for i in range(N):
        n = N-i-1
        a = (ord(alpha[i])-65) * 26**n
        ans += a

    if abs(ans - num) <= 100:
        print('nice')
    else:
        print('not nice')