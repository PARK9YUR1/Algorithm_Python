num = list(map(int, input().split()))
result = 0
for n in num:
    result += n ** 2
result %= 10
print(result)