while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0, 0]:
        break

    nums.sort()
    x, y, z = nums
    if x**2 + y**2 == z**2:
        print('right')
    else:
        print('wrong')
