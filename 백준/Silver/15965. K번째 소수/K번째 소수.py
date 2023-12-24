def is_prime(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for i in range(2, N+1):
        if prime[i]:
            for j in range(i*i, N+1, i):
                prime[j] = False
    return [i for i in range(N+1) if prime[i]]

K = int(input()) - 1
arr = is_prime(7400000)
print(arr[K])