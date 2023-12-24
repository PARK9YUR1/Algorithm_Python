def is_prime(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for i in range(2, N+1):
        if prime[i]:
            for j in range(i*i, N+1, i):
                prime[j] = False
    return [i for i in range(N+1) if prime[i]]

T = int(input())
for _ in range(T):
    N = int(input())
    nums = is_prime(N)
    for num in nums:
        cnt = 0
        while N % num == 0:
            N /= num
            cnt += 1
        if cnt:
            print(num, cnt)