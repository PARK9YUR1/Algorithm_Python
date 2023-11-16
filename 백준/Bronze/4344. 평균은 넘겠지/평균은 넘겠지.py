C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    N, score = arr[0], arr[1:]
    avg = sum(score)/N
    
    cnt = 0

    for sc in score:
        if sc > avg:
            cnt += 1
    
    result = '{:.3f}'.format(cnt/N * 100, 3)
    print(f"{result}%")