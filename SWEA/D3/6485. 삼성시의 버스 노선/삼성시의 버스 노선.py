T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 버스노선 개수
    lst = [0]*5001  # 정류장
    for _ in range(N):
        A, B = map(int, input().split())  # 노선 : A이상 B이하 정류장
        for i in range(A, B+1):
            lst[i] += 1
    P = int(input())  # 버스정류장 개수

    result = []
    for _ in range(P):
        C = int(input())  # 버스정류장 번호
        result.append(lst[C])
    print(f'#{tc}', *result)