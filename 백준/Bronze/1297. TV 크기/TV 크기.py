D, H, W = map(int, input().split())  # TV 대각선길이, 높이비율, 너비비율
# 대각선 = ((높이 ** 2 + 너비 ** 2))**0.5
x = D / ((H**2 + W**2) ** 0.5)

h, w = int(H*x), int(W*x)
print(h, w)