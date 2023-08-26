A, B = map(int, input().split())  # 가로, 세로 길이
cut = int(input())  # 잘라야하는 점선 개수
G = [0, B]  # 가로방향
S = [0, A]  # 세로방향
for _ in range(cut):
    dir, num = map(int, input().split())  # 가로방향(0)or세로방향(1), 점선 번호
    if dir == 0:
        G.append(num)
    else:
        S.append(num)

G.sort()
S.sort()

G_mx = 0
S_mx = 0

for i in range(len(G)-1):
    ans = G[i+1] - G[i]
    if G_mx < ans:
        G_mx = ans

for i in range(len(S)-1):
    ans = S[i+1] - S[i]
    if S_mx < ans:
        S_mx = ans

result = G_mx * S_mx
print(result)