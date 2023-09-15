import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 국가의 수 N, 비행기의 종류 M
    N, M = map(int, input().split())
    print(N-1)
    for _ in range(M):
        # a와 b를 왕복하는 비행기
        a, b = map(int, input().split())