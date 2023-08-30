from itertools import permutations

N, M = map(int, input().split())
nums = [x for x in range(1, N+1)]
perm = list(permutations(nums, M))

for i in range(len(perm)):
    print(*perm[i])
