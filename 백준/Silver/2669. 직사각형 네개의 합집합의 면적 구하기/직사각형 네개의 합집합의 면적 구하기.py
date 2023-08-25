box = [[0]*100 for _ in range(100)]
for _ in range(4):
    ax, ay, bx, by = map(int, input().split())
    ay, by = 100 - ay, 100 - by
    for y in range(by, ay):
        for x in range(ax, bx):
            box[y][x] += 1

result = 0
for i in range(100):
    for j in range(100):
        if box[i][j] > 0:
            result += 1

print(result)