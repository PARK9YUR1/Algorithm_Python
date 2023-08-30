N, K = map(int, input().split())  # 동전은 N종류, 가치 합 K
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)

result = 0
money = 0
for i in range(N):
    x = K // coin[i]
    result += x
    K -= x * coin[i]
    if K == 0:
        break
print(result)