import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = {}
for _ in range(N):
    name = input().rstrip()
    lst[name] = 1
for _ in range(M):
    name = input().rstrip()
    if name in lst:
        lst[name] += 1
    else:
        lst[name] = 1

result = []

cnt = 0
for k, v in lst.items():
    if v == 2:
        cnt += 1
        result.append(k)

result.sort()

print(cnt)
for i in result:
    print(i)