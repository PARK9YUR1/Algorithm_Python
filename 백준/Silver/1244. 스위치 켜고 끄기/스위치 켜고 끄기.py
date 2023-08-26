S = int(input())  # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 상태 (on:1, off:0)
N = int(input())  # 학생 수
for _ in range(N):
    gender, num = map(int, input().split())  # 성별(남:1, 여:2), 받은 수

    if gender == 1:
        for i in range(S):
            if (i + 1) % num == 0:
                if switch[i] == 1:
                    switch[i] = 0
                else:
                    switch[i] = 1
    else:
        for i in range(S//2):
            if 0 <= num - 1 + i < S and 0 <= num - 1 - i < S:
                if switch[num-1+i] == switch[num-1-i]:
                    if switch[num-1+i] == 1:
                        switch[num-1+i] = switch[num-1-i] = 0
                    else:
                        switch[num-1+i] = switch[num-1-i] = 1
                else:
                    break

print(*switch[:20])
print(*switch[20:40])
print(*switch[40:60])
print(*switch[60:80])
print(*switch[80:100])