def solution(plans):
    result = []
    
    N = len(plans)
    for i in range(N):
        hour, minute = map(int, plans[i][1].split(':'))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])  # 시작시간 순 정렬
    
    stack = []
    cur_time = plans[0][1]  # 현재 시간
    for i in range(N):
        while stack:
            cur_sj, cur_start, cur_task = plans[i]  # 다음과제
            subject, start, task = stack[-1]  # 이전과제
            
            cur_time = max(cur_time, start)  # 현재시간 : 현재시간과 이전과제 시작시간 중 큰 값
            end = cur_time + task  # 끝나는시간 : 현재시간 + 이전과제 소요시간

            if end > cur_start:  # 이전과제 끝나는 시간이 다음과제 시작시간보다 늦은 경우
                x = cur_start - cur_time  # 남은시간 : 다음과제 시작시간 - 현재시간
                stack[-1][2] = task - x  # 이전과제 소요시간 : 기존 소요시간 - 남은시간
                cur_time += x  # 현재시간 : 현재시간 + 남은시간
                break
            else:  # 이전과제 끝나는 시간이 다음과제 시작시간과 같거나 빠른경우
                stack.pop()  # 이전과제를 끝냄
                result.append(subject)  # 끝낸과제 담기
                cur_time += task  # 현재시간 : 현재시간 + 과제소요시간
                
        stack.append(plans[i])

    
    for i in range(len(stack)):  # stack에 남은 과제들 거꾸로 담아주기
        subject, s, t = stack.pop()
        result.append(subject)
    return result