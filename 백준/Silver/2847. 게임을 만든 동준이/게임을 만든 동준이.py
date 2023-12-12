# 2847
N = int(input())
scores = [int(input()) for _ in range(N)]
scores = scores[::-1]

result = 0
mn = scores[0]
for i in range(1, N):
    score = scores[i]
    if mn < score:
        x = score - mn + 1
        mn = min(mn, score-x)
        result += x
    elif mn == score:
        mn = min(mn, score-1)
        result += 1
    else:
        mn = min(mn, score)
print(result)