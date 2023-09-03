DP = [0]*91
DP[1] = 1
for i in range(2, 91):
    DP[i] = DP[i-1] + DP[i-2]

n = int(input())
print(DP[n])