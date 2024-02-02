while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0, 0, 0]:
        break

    result = 0

    while True:
        if nums[0] == nums[1] == nums[2] == nums[3]:
            break
        nums = [abs(nums[i]-nums[i-1]) for i in range(4)]
        result += 1

    print(result)