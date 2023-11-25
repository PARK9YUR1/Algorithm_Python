color = []

for _ in range(2):
    body, tail = input().split()
    if body not in color:
        color.append(body)
    if tail not in color:
        color.append(tail)

color.sort()

result = []

for b in color:
    for t in color:
        ans = f'{b} {t}'
        result.append(ans)

for res in result:
    print(res)