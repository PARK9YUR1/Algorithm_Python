N, K = map(int, input().split())
result = 1

for i in range(K+1, N+1):
    result *= i

for i in range(1, N-K+1):
    result //= i

print(result)