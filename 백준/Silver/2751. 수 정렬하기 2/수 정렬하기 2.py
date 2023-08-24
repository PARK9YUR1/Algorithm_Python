import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
nums.sort()
for n in nums:
    print(n)