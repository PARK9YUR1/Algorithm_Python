K = int(input())
nums = list(map(int, input().split()))
N = 0
for i in range(K):
    N += 2**i
x = N - len(nums)
y = 2**(K-1) - x
answer = []

while True:
    for i in range(K-1, -1, -1):
        tmp = []
        for j in range(len(nums)):
            a = nums.pop(j)
            tmp.append(a)
            if (i != K-1 and len(tmp) == 2 ** i) or (i == K-1 and len(tmp) == y):
                break
        answer.insert(0, tmp)
    if len(nums) == 0:
        break

for ans in answer:
    print(*ans)