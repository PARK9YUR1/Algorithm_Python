board = [list(input()) for _ in range(8)]
result = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if board[i][j] == 'F':
                result += 1
    else:
        for j in range(1, 8, 2):
            if board[i][j] == 'F':
                result += 1
print(result)

