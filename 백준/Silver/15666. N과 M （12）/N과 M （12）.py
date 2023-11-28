def BOJ15666():
    global arr

    if len(arr) == M:
        print(*arr)
        return

    for i in range(length):
        if arr and arr[-1] > nums[i]:
            continue

        arr.append(nums[i])
        BOJ15666()
        arr.pop()


N, M = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()
arr = []
length = len(nums)
BOJ15666()