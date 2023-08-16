T = 10
for tc in range(1, T+1):
    length = int(input())
    text = list(map(str, input()))
    stack = []
    new_txt = ''

    # 후위 표기법
    for t in text:
        if t.isdigit():
            new_txt += t
        elif t == '+':
            while len(stack) > 0 and stack[-1] == '+':
                plus = stack.pop()
                new_txt += plus
            stack.append(t)

    while len(stack) > 0:
        plus = stack.pop()
        new_txt += plus

    # 계산
    for nt in new_txt:
        if nt.isdigit():
            stack.append(int(nt))
        elif nt == '+':
            y = stack.pop()
            x = stack.pop()
            z = x + y
            stack.append(z)

    if len(stack) == 1:
        result = stack.pop()

    print(f'#{tc} {result}')