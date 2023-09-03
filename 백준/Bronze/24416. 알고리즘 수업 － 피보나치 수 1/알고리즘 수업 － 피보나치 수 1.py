n = int(input())
f = [0] * (n+1)
f[0], f[1] = 0, 1
for i in range(2, n+1):
    f[i] = f[i-1]+f[i-2]

cnt1 = f[n]
cnt2 = n-2
print(cnt1, cnt2)