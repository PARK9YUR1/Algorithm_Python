T, S = map(int, input().split())  # 시간, 술ox
# 아침 < 12 <= 점심 <= 16 < 저녁
# 1: 술 o, 0: 술 x

if 12 <= T <= 16 and S == 0:
    print(320)
else:
    print(280)