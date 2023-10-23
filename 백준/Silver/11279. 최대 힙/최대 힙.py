import heapq, sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if nums:
            x = heapq.heappop(nums)
            print(-x)
        else:
            print(0)
    elif n > 0:
        heapq.heappush(nums, -n)