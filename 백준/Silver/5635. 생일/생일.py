N = int(input())
lst = []
for _ in range(N):
    name, D, M, Y = map(str, input().split())
    D, M, Y = int(D), int(M), int(Y)
    lst.append((name, D, M, Y))
lst.sort(key=lambda x:(x[3], x[2], x[1]))

print(lst[-1][0])
print(lst[0][0])