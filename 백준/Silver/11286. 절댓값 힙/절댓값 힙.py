import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if len(arr) == 0:
            print(0)
            continue
        mn = heapq.heappop(arr)[1]
        print(mn)