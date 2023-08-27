N = int(input())
nums = list(map(int, input().split()))

sosu = 0
for i in range(N):
    cnt = 0
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 0 and nums[i] != 1:
        sosu += 1
print(sosu)