M = int(input())
x = 1

for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    if x == a:
        x = b
    elif x == b:
        x = a

print(x)