N, K = map(int, input().split())
nums = list(input())
stack = []

for num in nums:
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -=1
    stack.append(num)

if K > 0:
    print(''.join(stack)[:len(stack)-K])
else:
    print(''.join(stack))