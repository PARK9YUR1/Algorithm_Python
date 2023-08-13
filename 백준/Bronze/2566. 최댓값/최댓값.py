box = [list(map(int, input().split())) for _ in range(9)]

mx = 0
mx_i = 0
mx_j = 0

for i in range(9):
    for j in range(9):
        if mx <= box[i][j]:
            mx = box[i][j]
            mx_i = i + 1
            mx_j = j + 1

print(mx)
print(mx_i, mx_j)