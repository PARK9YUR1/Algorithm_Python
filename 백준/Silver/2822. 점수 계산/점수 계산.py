# 2822
arr = [[i, int(input())] for i in range(1, 9)]
arr.sort(key=lambda x:-x[1])
nums = [x[0] for x in arr[:5]]
nums.sort()
total = [x[1] for x in arr[:5]]
print(sum(total))
print(*nums)