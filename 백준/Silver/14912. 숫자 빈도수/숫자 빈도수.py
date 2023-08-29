N, D = map(int, input().split())

result = 0
for i in range(1, N+1):
    result += str(i).count(str(D))

print(result)