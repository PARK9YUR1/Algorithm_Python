# 2630
# 1:파란색, 0:하얀색

def paper(x, y, n):
    global W, B
    white = blue = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == 0:
                white += 1
            elif arr[i][j] == 1:
                blue += 1
    if white == n**2:
        W += 1
        return
    elif blue == n**2:
        B += 1
        return
    else:
        z = n // 2
        paper(x, y, z)
        paper(x + z, y, z)
        paper(x, y + z, z)
        paper(x + z, y + z, z)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
W = B = 0

paper(0, 0, N)
print(W)
print(B)