def solution(n):
    n = str(n)
    ans = 0
    
    for i in n:
        ans += int(i)
    
    return ans