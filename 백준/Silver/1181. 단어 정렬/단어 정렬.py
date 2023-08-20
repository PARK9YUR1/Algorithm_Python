N = int(input())
words = [[] for _ in range(51)]
check_list = []

for _ in range(N):
    word = input()
    if word in check_list:
        continue
    check_list.append(word)

    words[len(word)].append(word)
    words[len(word)].sort()

for i in range(len(words)):
    if len(words[i]) > 0:
        for j in range(len(words[i])):
            print(words[i][j])