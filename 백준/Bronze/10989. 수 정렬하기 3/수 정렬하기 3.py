import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = [0] * 10001
for _ in range(N):
    num = int(input().rstrip())
    nums[num] += 1

for i in range(len(nums)):
    for _ in range(nums[i]):
        print(i)
