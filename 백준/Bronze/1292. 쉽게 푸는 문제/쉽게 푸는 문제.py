import sys
input = sys.stdin.readline

A, B = map(int, input().split())
nums = []
for i in range(1, 1001):
    if len(nums) >= B:
        break
    for _ in range(1, i+1):
        nums.append(i)

print(sum(nums[A-1:B]))