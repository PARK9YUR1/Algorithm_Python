import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
q, result = [], 0

for i in range(N):
    start, end = arr[i]
    heapq.heappush(q, end)
    while q[0] <= start:
        heapq.heappop(q)
    result = max(result, len(q))

print(result)