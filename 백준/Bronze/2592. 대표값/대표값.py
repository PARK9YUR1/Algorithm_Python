nums = [int(input()) for _ in range(10)]
arr = [(nums.count(num), num) for num in nums]
arr.sort(reverse=True)
print(sum(nums)//10)
print(arr[0][1])