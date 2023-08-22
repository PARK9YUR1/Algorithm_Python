N = int(input())
nums = []
for _ in range(N):
    x = int(input())
    nums.append(x)

nums.sort()

for num in nums:
    print(num)