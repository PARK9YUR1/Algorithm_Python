def is_prime(A, B):
    prime = [True]*(B+1)
    prime[0] = prime[1] = False

    for i in range(2, B+1):
        if prime[i]:
            for j in range(i*i, B+1, i):
                prime[j] = False
    return [str(i) for i in range(B+1) if prime[i] and A <= i <= B]


A, B, D = map(int, input().split())
primes = is_prime(A, B)
D = str(D)
result = 0
for prime in primes:
    if D in prime:
        result += 1
print(result)