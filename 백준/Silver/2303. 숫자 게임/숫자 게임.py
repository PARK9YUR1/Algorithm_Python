from itertools import permutations

N = int(input())
lst = [0] * N
for i in range(N):
    nums = list(map(int, input().split()))
    perm = list(permutations(nums, 3))
    mx = 0
    for j in range(len(perm)):
        mx = max(mx, sum(perm[j])%10)
    lst[i] = mx

result = N - lst[::-1].index(max(lst))
print(result)