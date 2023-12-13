# 5052
T = int(input())
for _ in range(T):
    N = int(input())
    result = 'YES'
    nums = [input() for _ in range(N)]
    nums.sort()
    num = nums[0]

    for i in range(1, N):
        length = len(num)
        if nums[i][:length] == num:
            result = 'NO'
        num = nums[i]

    print(result)