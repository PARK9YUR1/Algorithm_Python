def subset(N, i):
    global M, J, code
    if i == N:
        if sum(bits) == L and M >= 1 and J >= 2:
            code.sort()
            cd = ''.join(code)
            result.append(cd)
        return

    bits[i] = 1
    if alpha[i] in 'aeiou':
        M += 1
    else:
        J += 1
    code.append(alpha[i])
    subset(N, i+1)

    bits[i] = 0
    if alpha[i] in 'aeiou':
        M -= 1
    else:
        J -= 1
    code.pop(code.index(alpha[i]))
    subset(N, i+1)

L, C = map(int, input().split())  # L:암호개수, C:주어진 알파벳 개수
alpha = list(map(str, input().split()))
bits = [0]*C
M = J = 0  # 모음, 자음
code, result = [], []
subset(C, 0)
result.sort()
for x in result:
    print(x)