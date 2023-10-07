N = int(input())
txt = [input() for _ in range(N)]
length = len(txt[0])
arr = [[] for _ in range(length)]

for i in range(N):
    for j in range(length):
        arr[j].append(txt[i][j])
        arr[j] = list(set(arr[j]))

result = ''
for x in arr:
    if len(x) == 1:
        result += x[0]
    else:
        result += '?'

print(result)