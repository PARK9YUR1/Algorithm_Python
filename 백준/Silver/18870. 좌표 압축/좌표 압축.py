import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
lst = sorted(set(nums[::]))

result = {}
for i in range(len(lst)):
    result[lst[i]] = i

for n in nums:
    print(result[n], end=' ')