# 4949 균형잡힌 세상

# import sys
# input = sys.stdin.readline
txt = ''

while True:
    stack = []
    result = 'yes'
    txt = ''.join(list(map(str, input())))

    if txt == '.':
        break

    for x in txt:
        if x in '([':
            stack.append(x)
        elif x in ')]':
            if len(stack) == 0:
                result = 'no'
                break
            if x == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
            elif x == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
                    break

    if len(stack) > 0:
        result = 'no'

    print(result)