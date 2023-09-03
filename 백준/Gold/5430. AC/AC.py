from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = tuple(input().rstrip())
    N = int(input())  # 배열에 들어있는 수 개수
    nums = deque()
    num = ''
    for i in input():
        if i in ',]' and num.isdigit():
            nums.append(num)
            num = ''
        elif i.isdigit():
            num += i

    result = ''
    cnt = 0
    for p in P:
        if p == 'R':
            cnt += 1
        elif p == 'D':
            if len(nums) == 0:
                result = 'error'
                break
            if cnt % 2 == 1:
                nums.pop()
            else:
                nums.popleft()

    if result != 'error':
        if cnt % 2 == 0:
            result = '[' + ','.join(tuple(nums)) + ']'
        else:
            result = '['
            for i in range(len(nums)-1, -1, -1):
                if i != 0:
                    result += nums[i] + ','
                else:
                    result += nums[i]
            result += ']'

    print(result)