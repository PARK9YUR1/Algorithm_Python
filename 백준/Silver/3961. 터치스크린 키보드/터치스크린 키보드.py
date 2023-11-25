# 3961

keyboards = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ''],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', '', '', ''],
]

keyboards_xy = {}

def find_xy(alpha):
    for i in range(3):
        for j in range(10):
            if keyboards[i][j] == alpha:
                keyboards_xy[alpha] = [i, j]

for i in range(97, 123):
    find_xy(chr(i))


t = int(input())
for _ in range(t):
    word, num = input().split()
    words = []

    n = int(num)
    for _ in range(n):
        txt = input()
        result = 0
        for i in range(len(word)):
            if word[i] == txt[i]:
                continue
            else:
                w, t = word[i], txt[i]
                result += (abs(keyboards_xy[w][0] - keyboards_xy[t][0]) +
                           abs(keyboards_xy[w][1] - keyboards_xy[t][1]))
        words.append([txt, result])

    words.sort(key=lambda x:(x[1], x[0]))

    for wd in words:
        print(*wd)
