H, M, S = map(int, input().split())
time = int(input())

s = time % 60
time -= s
time //= 60
m = time % 60
time -= m
time //= 60
h = time

S += s
if S >= 60:
    S -= 60
    M += 1
M += m
if M >= 60:
    M -= 60
    H += 1
H += h
while H >= 24:
    H -= 24

print(H, M, S)