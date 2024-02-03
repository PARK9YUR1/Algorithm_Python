N, W, H = map(int, input().split())
x = (W**2 + H**2)**0.5
for _ in range(N):
    n = int(input())
    if n <= x:
        print('DA')
    else:
        print('NE')
