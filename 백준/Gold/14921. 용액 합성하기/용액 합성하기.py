N = int(input())
nums = list(map(int, input().split()))
nums.sort(key=lambda x:abs(x))

start, end = 0, 1
mn_abs = 10 ** 10
result = 0
while True:
    if end == N:
        break
    ans = nums[start] + nums[end]
    if mn_abs > abs(ans):
        mn_abs = abs(ans)
        result = ans
    start, end = start+1, end+1

print(result)