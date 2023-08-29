N = int(input())
nums = [(x+1) for x in range(N)]
result = []
while True:
    a = nums.pop(0)
    result.append(a)
    if len(nums) == 0:
        break
    b = nums.pop(0)
    nums.append(b)
    if len(nums) == 0:
        break
print(*result)