import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 나무 수, 필요한 나무 길이
tree = list(map(int, input().split()))
tree.sort()
start, end = 0, max(tree)

while start <= end:
    middle = (start + end) // 2
    total = 0

    for t in tree:
        if t > middle:
            total += t - middle

    if total >= M:
        start = middle + 1
    else:
        end = middle - 1

print(end)