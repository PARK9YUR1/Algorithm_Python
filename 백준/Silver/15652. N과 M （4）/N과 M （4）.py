import sys
input = sys.stdin.readline

def NM(x):
    if x == M:
        arr = checked[:]
        arr.sort()
        if arr == checked:
            print(*checked)
        return
    for i in range(1, N+1):
        checked[x] = i
        NM(x+1)
        checked[x] = 0

# N개 중 M개 고르기 (오름차순으로)
N, M = map(int, input().split())
checked = [0]*M
NM(0)