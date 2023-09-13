def Rev(n):
    return int(str(n)[::-1])
X, Y = map(int, input().split())
result = Rev(Rev(X)+Rev(Y))
print(result)