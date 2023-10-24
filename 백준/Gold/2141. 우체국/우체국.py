import sys
input = sys.stdin.readline

N = int(input())
arr = []
people = 0

for _ in range(N):
    x, a = map(int, input().split())
    arr.append((x, a))
    people += a
arr.sort()

cnt = 0
for i in range(N):
    cnt += arr[i][1]
    if cnt >= people/2:
        print(arr[i][0])
        break