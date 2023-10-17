from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

arr = list(permutations(nums, M))
arr.sort()
for lst in arr:
    print(*lst)