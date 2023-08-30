import sys
input = sys.stdin.readline

A, B = map(int, input().split())  # A, B 원소 개수
result = {}
for num in input().split():
    if num in result:
        result[num] += 1
    else:
        result[num] = 1
for num in input().split():
    if num in result:
        result[num] += 1
    else:
        result[num] = 1

cnt = 0
for k, v in result.items():
    if v == 1:
        cnt += 1
print(cnt)