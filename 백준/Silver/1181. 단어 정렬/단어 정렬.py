N = int(input())
words = [[] for _ in range(51)]

for _ in range(N):
    word = input()

    if word not in words[len(word)]:
        words[len(word)].append(word)
        words[len(word)].sort()

for i in range(len(words)):
    if len(words[i]) > 0:
        for j in range(len(words[i])):
            print(words[i][j])