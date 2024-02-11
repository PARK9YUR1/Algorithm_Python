arr = [int(input()) for _ in range(9)]
arr.sort()

x = sum(arr) - 100
a = b = 0

for i in range(9):
    for j in range(i+1, 9):
        if a or b:
            break
        if arr[i] + arr[j] == x:
            a, b = i, j
            break

if b < 9:
    result = arr[:a] + arr[a+1:b] + arr[b+1:]
else:
    result = arr[:a] + arr[a+1:]

for res in result:
    print(res)