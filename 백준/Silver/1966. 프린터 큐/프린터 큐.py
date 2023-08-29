T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    idx = [x for x in range(N)]
    J = list(map(int, input().split()))

    cnt = 0
    while True:
        if M not in idx:
            break
        check = True
        for i in range(len(J)):
            if J[0] < J[i]:
                check = False
                break
        if check == False:
            x = J.pop(0)
            J.append(x)
            y = idx.pop(0)
            idx.append(y)
        else:
            cnt += 1
            J.pop(0)
            idx.pop(0)
    print(cnt)