N, K = map(int, input().split())
score = [0] * (N+1)

for _ in range(N):
    C, G, S, D = map(int, input().split())
    score[C] = G*3 + S*2 + D*1

result = 1
for i in range(N):
    if i == K:
        continue
    if score[i] > score[K]:
        result += 1

print(result)