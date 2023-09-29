def coloring1(arr):
    cnt = 0
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0 and arr[i][j] != 'B':
                    cnt += 1
                elif j % 2 == 1 and arr[i][j] != 'W':
                    cnt += 1
        else:
            for j in range(8):
                if j % 2 == 0 and arr[i][j] != 'W':
                    cnt += 1
                elif j % 2 == 1 and arr[i][j] != 'B':
                    cnt += 1
    return cnt

def coloring2(arr):
    cnt = 0
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0 and arr[i][j] != 'W':
                    cnt += 1
                elif j % 2 == 1 and arr[i][j] != 'B':
                    cnt += 1
        else:
            for j in range(8):
                if j % 2 == 0 and arr[i][j] != 'B':
                    cnt += 1
                elif j % 2 == 1 and arr[i][j] != 'W':
                    cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

mn = 10 ** 6
for i in range(N-7):
    for j in range(M-7):
        new_board = [board[k][j:j+8] for k in range(i, i+8)]
        mn_value = min(coloring1(new_board), coloring2(new_board))
        mn = min(mn, mn_value)
print(mn)