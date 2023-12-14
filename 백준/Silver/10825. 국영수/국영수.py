# 10825
N = int(input())
arr = [input().split() for _ in range(N)]
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for x in arr:
    name = x[0]
    print(name)