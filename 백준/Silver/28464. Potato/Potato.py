from collections import deque
import sys
input = sys.stdin.readline

N = int(input())  # 접시 개수
lst = list(map(int, input().split()))  # 접시에 있는 감자튀김
lst.sort()
lst = deque(lst)

S = P = 0  # 성우(최소), 박모씨(최대)
while True:
    P += lst.pop()
    if len(lst) == 0:
        break
    S += lst.popleft()
    if len(lst) == 0:
        break

print(S, P)