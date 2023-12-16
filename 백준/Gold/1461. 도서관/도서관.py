# 1461
N, M = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

idx = -1
for i in range(N):
    if books[i] > 0:
        idx = i
        break

left, right = books[:idx], books[idx:][::-1]
if idx == -1: left, right = [abs(book) for book in books], []
l, r = [], []

if left:
    for i in range(len(left)):
        if i % M == 0:
            l.append(abs(left[i]))
if right:
    for i in range(len(right)):
        if i % M == 0:
            r.append(right[i])


if len(left) == 0:
    mx = right[0]
elif len(right) == 0:
    mx = left[0]
else:
    mx = max(l[0], r[0])

result = 0
for dist in l:
    result += dist * 2
for dist in r:
    result += dist * 2
result -= mx
print(result)
