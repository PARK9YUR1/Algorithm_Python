N = int(input())  # 수열의 길이
nums = [int(input()) for _ in range(N)]

if nums[2]-nums[1] == nums[1]-nums[0]:
    d = nums[1]-nums[0]
    print(nums[-1]+d)
else:
    r = nums[1]//nums[0]
    print(nums[-1]*r)