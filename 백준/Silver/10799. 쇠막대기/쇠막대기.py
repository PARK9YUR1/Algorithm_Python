import sys
input = sys.stdin.readline

lst = [' '] + list(map(str, input().rstrip())) + [' ']
left_cnt = 0
result = 0
for i in range(1, len(lst)-1):
    l = lst[i-1]
    c = lst[i]
    r = lst[i+1]
    if c == '(' and r == ')':
        result += left_cnt
    if c == '(' and r != ')':
        left_cnt += 1
    elif c == ')' and l != '(':
        result += 1
        left_cnt -= 1
        pass
print(result)