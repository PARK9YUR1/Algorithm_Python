while True:
    nums = list(input())
    if nums == ['0']:
        break

    result = 1
    result += len(nums)
    for num in nums:
        if num == '1':
            result += 2
        elif num == '0':
            result += 4
        else:
            result += 3
    print(result)