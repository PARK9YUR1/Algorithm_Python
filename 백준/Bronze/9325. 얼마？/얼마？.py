# 9325

T = int(input())
for _ in range(T):
    s = int(input())
    result = s

    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        result += q*p

    print(result)