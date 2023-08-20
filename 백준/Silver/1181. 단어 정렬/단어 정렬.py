N = int(input())
words = [[] for _ in range(51)]

for _ in range(N):
    word = input()
    check = True
    for w in word:
        if w.isdigit() == True:
            check = False
            break
    if check == True and word not in words[len(word)]:
        words[len(word)].append(word)
        words[len(word)].sort()

for i in range(len(words)):
    if len(words[i]) > 0:
        for j in range(len(words[i])):
            print(words[i][j])