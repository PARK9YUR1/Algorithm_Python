box = [list(map(str, input())) for _ in range(5)]

mx_len = 0
for i in box:
    if mx_len <= len(i):
        mx_len = len(i)
for i in box:
    if len(i) < mx_len:
        d = mx_len - len(i)
        for _ in range(d):
            i.append('')

for j in range(mx_len):
    for i in range(5):
        print(box[i][j], end='')