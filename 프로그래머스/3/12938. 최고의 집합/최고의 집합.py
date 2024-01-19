def solution(n, s):
    answer = []
    a = s // n
    b = s % n
    if a == 0:
        answer = [-1]
    else:
        if not b:
            answer = [a]*n
        else:
            answer = [a]*(n-b)
            answer += [a+1]*b
    return answer