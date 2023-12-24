def is_prime(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for i in range(2, N+1):
        if prime[i]:
            for j in range(i*i, N+1, i):
                prime[j] = False
    return [i for i in range(N+1) if prime[i]]


primes = is_prime(100000)
while True:
    nums = input()
    if nums == '0':
        break
    N = len(nums)

    mx = 0
    for i in range(N):
        for j in range(i, N):
            num = int(nums[i:j+1])
            if num in primes:
                mx = max(num, mx)
    print(mx)