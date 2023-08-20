N = int(input())
words = [[] for _ in range(51)]
mx_len = 0

for _ in range(N):
    word = input()

    if word not in words[len(word)]:
        words[len(word)].append(word)
        words[len(word)].sort()

    if mx_len < len(word):
        mx_len = len(word)

for i in range(1, mx_len + 1):
    if len(words[i]) > 0:
        for j in range(len(words[i])):
            print(words[i][j])