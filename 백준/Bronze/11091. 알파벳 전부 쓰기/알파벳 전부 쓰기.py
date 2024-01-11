N = int(input())
for _ in range(N):
    missing = ''
    alpha = {}
    for i in range(97, 123):
        alpha[i] = 0
    txt = input()

    for t in txt:
        if 65 <= ord(t) <= 90:
            alpha[ord(t)+32] += 1
        elif 97 <= ord(t) <= 122:
            alpha[ord(t)] += 1

    for a in alpha:
        if not alpha[a]:
            missing += chr(a)

    if missing:
        print(f'missing {missing}')
    else:
        print('pangram')