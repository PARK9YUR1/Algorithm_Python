nums = []
mn = 100
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        nums.append(num)
        mn = min(num, mn)
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(mn)