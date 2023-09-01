alpha = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
        '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
number = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
        'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
M, N = map(int, input().split())
nums = [str(n) for n in range(M, N+1)]
new_nums = []
for i in range(len(nums)):
    n = ''
    for j in range(len(nums[i])):
        n += alpha[nums[i][j]] + ' '
    new_nums.append(n.rstrip().split())
new_nums.sort()

for i in range(len(new_nums)):
    for j in range(len(new_nums[i])):
        new_nums[i][j] = number[new_nums[i][j]]

cnt = 0
for num in new_nums:
    cnt += 1
    print(''.join(num), end=' ')
    if cnt % 10 == 0:
        print()
