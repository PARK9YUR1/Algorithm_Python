def solution(plans):
    result = []
    N = len(plans)
    for i in range(N):
        hour, minute = map(int, plans[i][1].split(':'))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])  # 시작시간 순 정렬
    
    # hour, minute = plans[-1][1]
    # t = plans[-1][2]
    # hour, minute = hour+(minute+t)//60, (minute+t)%60
    
    # plans = plans + [['last', plans[-1][1]+plans[-1][2], plans[-1][2]]]
    print('plans', plans)
    
    stack = []
    cur_time = plans[0][1]
    for i in range(N):
        while stack:
            cur_sj, cur_start, cur_task = plans[i]
            
            subject, start, task = stack[-1]
            cur_time = max(cur_time, start)
            
            end = cur_time + task
            
            print(f'과목{subject}, cur_time {cur_time}, end {end}, cur_start {cur_start}')
            if end > cur_start:
                x = cur_start - cur_time  # 남은시간
                stack[-1][2] = task - x
                cur_time += x
                break
            else:
                stack.pop()
                result.append(subject)
                cur_time += task
                
        stack.append(plans[i])
        # print(i, stack)
    
    print(result)
    
    for i in range(len(stack)):
        subject, s, t = stack.pop()
        result.append(subject)
    return result
    
#     # cur_h, cur_m = plans[0][1]
#     end_h, end_m = plans[0][1]
    
#     stack = []
    
#     for i in range(N):
#         subject, start, time = plans[i]
#         start_h, start_m = start
#         # end_h, end_m = start_h+(start_m+t)//60, (start_m+t)%60
        
#         while stack:
#             sj, s, t = stack[-1]
#             end_h, end_m = end_h+(end_m+t)//60, (end_m+t)%60
#             end = [end_h, end_m]
#             print(f'end{end} / s{start}')
#             if end > start:  # 이전과제 끝나는시간이 다음과제 시작시간보다 늦으면
#                 end_time = end_h * 60 + end_m
#                 start_time = start[0]*60 + start[1]
#                 print(f'남은시간 end {end_h}:{end_m} / start {start[0]}:{start[1]}')
#                 x = end_time - start_time  # 남은시간
#                 print('xxxxxx', x)
#                 # cur_h, cur_m = 
#                 stack[-1][2] = t-x
#                 break
#             else:
#                 # end_h, end_m = end_h+(end_m+t)//60, (end_m+t)%60
#                 stack.pop()
#                 result.append(sj)
                
#         stack.append(plans[i])
#         print(i, stack)
    
#     return result

# # def solution(plans):
# #     N = len(plans)
# #     for i in range(N):
# #         plans[i][1] = plans[i][1].split(':')
# #         plans[i][1][0], plans[i][1][1] = int(plans[i][1][0]), int(plans[i][1][1])
# #         plans[i][2] = int(plans[i][2])
# #     plans.sort(key=lambda x: x[1])  # 시작시간 순 정렬
# #     print('plans', plans)
    
# #     hour, minute = plans[-1][1]
# #     t = plans[-1][2]
# #     hour, minute = hour+(minute+t)//60, (minute+t)%60
# #     plans = plans + [['last', [hour, minute], plans[-1][2]]]
# #     # print('arr', arr)
    
# #     result, stack = [], []
# #     cur_h, cur_m = 0, 0
# #     for i in range(N+1):
# #         cur_subject, cur_start, cur_time = plans[i]
# #         cur_h, cur_m = cur_start
# #         t = 0
        
# #         while stack:
# #             subject, start, time = stack[-1]
# #             h, m = start

# #             times = h*60 + m
# #             cur_times = cur_h*60 + cur_m

# #             x = cur_times - times - t # 남은 시간
# #             print(f'==== 과제 {stack[-1]} 현재 시간 {cur_h}:{cur_m}, 남은 시간 {x}, 과제 소요시간 {time}')
# #             if x < time:  # 남은 시간보다 이전 과제 소요시간이 클 때
# #                 stack[-1][2] = time - x  # 남은 시간만큼 이전 과제를 진행후, 소요시간 갱신
# #                 # print('stackkkkkkk', stack)
# #                 break
# #             else:
# #                 stack.pop()
# #                 result.append(subject)
# #                 # cur_h, cur_m = cur_h+(cur_m+cur_time)//60, (cur_m+cur_time)%60
# #                 t += time
        
# #         stack.append(plans[i])
# #         print(i, stack, '//', result)

    
# #     return result
