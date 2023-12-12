# 1946
T = int(input())
for _ in range(T):
    N = int(input())
    # (서류성적순위, 면접성적순위)
    scores = [tuple(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x:(x[0], x[1]))
    result = N
    x = scores[0][1]
    for score in scores:
        y = score[1]
        if x < y:
            result -= 1
        x = min(x, y)
    print(result)