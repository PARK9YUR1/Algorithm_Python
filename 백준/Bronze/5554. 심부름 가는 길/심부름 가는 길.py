time = [int(input()) for _ in range(4)]
total = sum(time)
h = total // 60
m = total % 60
print(h)
print(m)