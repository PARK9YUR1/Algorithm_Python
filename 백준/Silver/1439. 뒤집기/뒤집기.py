S = input()
x = S[0]
cnt1 = 1
cnt2 = 0
for i in range(1, len(S)):
    if S[i] == x:
        if S[i-1] != x:
            cnt1 += 1
    else:
        if S[i-1] == x:
            cnt2 += 1
print(min(cnt1, cnt2))
