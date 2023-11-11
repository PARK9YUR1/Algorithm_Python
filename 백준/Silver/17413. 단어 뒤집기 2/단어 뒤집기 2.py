txt = input()

stack = []
result = []

for t in txt:
    if t == '<':
        if stack:
            result += stack[::-1]
            stack = [t]
        else:
            stack.append(t)
    elif t == '>':
        stack.append(t)
        result += stack
        stack = []
    elif t == ' ':
        if '<' not in stack:
            result += stack[::-1]
            result.append(t)
            stack = []
        else:
            stack.append(t)
    else:
        stack.append(t)

if stack:
    result += stack[::-1]

print(''.join(result))