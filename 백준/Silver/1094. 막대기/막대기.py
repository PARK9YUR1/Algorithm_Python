# 1094
length = 64
X = int(input())

arr = [length]
while True:
    if sum(arr) == X:
        break

    mn = arr.pop()
    length = mn / 2
    if length > X:
        arr.append(length)
    else:
        arr.append(length)
        if sum(arr) < X:
            arr.append(length)

print(len(arr))