a, b = map(int, input().split())
a = int(str(a), 2)
b = int(str(b), 2)
print(bin(a+b)[2:])