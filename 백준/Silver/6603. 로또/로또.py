def subset(N, i):
    if i == N:
        if sum(bits) == 6:
            for j in range(N):
                if bits[j] == 1:
                    print(nums[j], end=' ')
            print()
        return
    bits[i] = 1
    subset(N, i+1)
    bits[i] = 0
    subset(N, i+1)

while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    k, nums = lst[0], lst[1:]
    bits = [0] * k
    subset(k, 0)
    print()