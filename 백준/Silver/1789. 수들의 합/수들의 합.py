# 1789
# 서로 다른 N개의 자연수 합이 S, 자연수 N의 최대값 구하기
S, N = int(input()), 0
total = 0

for i in range(1, S+1):
    total += i
    N += 1
    if total > S:
        N -= 1
        break

print(N)