cnt = [0, 0, 0, 0]
for i in range(4):
    minus, plus = map(int, input().split())
    if i > 0:
        cnt[i] += cnt[i-1]
    cnt[i] += plus
    cnt[i] -= minus
print(max(cnt))