N = int(input())
nums = [int(input()) for _ in range(N)]
if nums.count(0) > nums.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
