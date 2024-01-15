for _ in range(3):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    s = sum(nums)
    if s < 0:
        print('-')
    elif s == 0:
        print(0)
    else:
        print('+')