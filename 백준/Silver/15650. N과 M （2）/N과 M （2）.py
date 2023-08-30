from itertools import permutations

N, M = map(int, input().split())
nums = [x for x in range(1, N+1)]
perm = list(permutations(nums, M))

for i in range(len(perm)):
    check = True
    for j in range(M-1):
        if M == 1:
            break
        if perm[i][j] >= perm[i][j+1]:
            check = False
            break
    if check == True:
        print(*perm[i])