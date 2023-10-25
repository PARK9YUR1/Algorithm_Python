# 세준이의 체력은 100, 기쁨은 0
N = int(input())
power = [0] + list(map(int, input().split()))  # 인사 할 때 잃는 체력
joy = [0] + list(map(int, input().split()))  # 인사 할 때 얻는 기쁨

DP = [[0 for _ in range(101)] for _ in range(N+1)]
# DP[i][j] : i번째 사람에게 얻은 기쁨, 체력 j
# 체력이 j일 때 얻을 수 있는 최대 기쁨

for i in range(1, N+1):
    for j in range(1, 101):
        if power[i] <= j:
            # 현재 기쁨 + 남은 체력만큼 인사를 했을 때 기쁨 or 이전까지 기쁨 -> 더 큰 값
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-power[i]] + joy[i])
        else:
            DP[i][j] = DP[i-1][j]

print(DP[N][99])