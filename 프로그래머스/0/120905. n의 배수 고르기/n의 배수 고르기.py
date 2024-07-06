def solution(n, numlist):
    answer = []
    
    for num in numlist:
        if num%n:
            continue
        answer.append(num)
            
    return answer