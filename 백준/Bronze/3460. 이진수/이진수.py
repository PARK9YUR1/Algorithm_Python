T = int(input())
for _ in range(T):
    n = int(input())
    num = bin(n)[2:][::-1]
    result = [i for i in range(len(num)) if num[i] == '1']
    print(*result)