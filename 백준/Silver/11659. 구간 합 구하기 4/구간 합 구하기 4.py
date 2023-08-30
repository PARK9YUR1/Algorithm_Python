import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hab = [0] * N
nums = list(map(int, input().split()))
hab[0] = nums[0]

for i in range(1, N):
    hab[i] = hab[i-1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        result = hab[j-1]
    else:
        result = hab[j-1] - hab[i-2]
    print(result)