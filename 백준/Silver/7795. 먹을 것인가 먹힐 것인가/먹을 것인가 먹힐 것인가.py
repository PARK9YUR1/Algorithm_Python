T = int(input())
for _ in range(T):
    N, M = map(int, input().split())  # A의 수 N / B의 수 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    result = 0
    for i in range(N):
        start, end = 0, M-1
        while start <= end:
            mid = (start + end) // 2
            if B[mid] >= A[i]:
                end = mid - 1
            else:
                start = mid + 1
        result += end+1

    print(result)