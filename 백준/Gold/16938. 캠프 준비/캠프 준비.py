def question(i):
    global bits, cnt
    total = 0
    mx, mn = 0, 10**6
    if i == N:
        for j in range(N):
            if bits[j] == 1:
                mx = max(A[j], mx)
                mn = min(A[j], mn)
                total += A[j]
        if L <= total <= R and mx-mn >= X:
            cnt += 1
        return

    bits[i] = 1
    question(i+1)
    bits[i] = 0
    question(i+1)

# 문제 N개,   L <= 난이도 합 <= R,   난이도 (최상)-(최하) >= X
N, L, R, X = map(int, input().split())
A = list(map(int, input().split())) # 문제 난이도
cnt = 0
bits = [0]*N
question(0)
print(cnt)