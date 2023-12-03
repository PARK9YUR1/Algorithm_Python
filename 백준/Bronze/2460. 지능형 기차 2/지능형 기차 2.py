train = [0]*11
cnt = 0
for i in range(1, 11):
    a, b = map(int, input().split())  # 내린사람, 탄사람
    cnt += b
    cnt -= a
    train[i] = cnt
print(max(train))