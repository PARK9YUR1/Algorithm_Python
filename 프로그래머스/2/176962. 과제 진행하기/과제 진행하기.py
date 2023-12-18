def solution(plans):
    N = len(plans)
    plans.sort(key=lambda x: x[1])  # 시작시간 순 정렬
    for i in range(N):
        start, end = plans[i][1], plans[i][2]
        minute = int(start[3:]) + int(end)
        h = f'{minute // 60 + int(start[:2])}'.zfill(2)
        m = f'{minute % 60}'.zfill(2)
        plans[i][2] = f'{h}:{m}'

    stack = []
    result = []

    for i in range(N):
        if stack:
            sj, S, E = stack[-1]
            subject, start, end = plans[i]
            print('i E start', i, E, start)
            if E <= start:
                result.append(sj)
                stack.pop()

                if i == N-1:
                    result.append(subject)
                    while stack:
                        x = stack.pop()
                        result.append(x[0])
                else:
                    while True:
                        if stack:
                            sj, S, E = stack[-1]
                            if E <= start:
                                result.append(sj)
                                stack.pop()
                            else:
                                break
                        else:
                            break
        stack.append(plans[i])

    print(plans)
    return result