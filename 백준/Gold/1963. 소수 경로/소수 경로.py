def is_prime(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for i in range(2, N+1):
        if prime[i]:
            for j in range(i*i, N+1, i):
                prime[j] = False
    return [str(i) for i in range(N+1) if prime[i] and i >= 1000]

primes = is_prime(9999)

def bfs(s, e):
    q = [(str(s), 0)]

    visited = [False]*10000
    visited[s] = 1

    while q:
        num, cnt = q.pop(0)
        if num == str(e):
            return cnt

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                new = int(num[:i] + str(j) + num[i+1:])
                if not visited[new] and str(new) in primes:
                    visited[new] = True
                    q.append((str(new), cnt+1))


T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    if s == e:
        print(0)
        continue
    result = bfs(s, e)
    if result:
        print(result)
    else:
        print('Impossible')