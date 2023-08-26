N = int(input())  # 수열 길이
nums = list(map(int, input().split()))

mx = 1
length = 1
for i in range(N-1):
    if nums[i] <= nums[i+1]:
        length += 1
    else:
        mx = max(mx, length)
        length = 1
    mx = max(mx, length)

length = 1
for i in range(N-1):
    if nums[i] >= nums[i+1]:
        length += 1
    else:
        mx = max(mx, length)
        length = 1
    mx = max(mx, length)

print(mx)