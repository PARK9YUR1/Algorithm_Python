X = input()
cnt = 0

while True:
    if len(X) == 1:
        n = int(X)
        break
    cnt += 1
    n = 0
    for i in X:
        n += int(i)
    X = str(n)

result = 'NO'
if n in [3, 6, 9]:
    result = 'YES'
print(cnt)
print(result)