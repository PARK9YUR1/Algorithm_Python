import sys
input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().split()))
M = int(input())

for num in input().split():
    if int(num) in nums:
        print(1)
    else:
        print(0)