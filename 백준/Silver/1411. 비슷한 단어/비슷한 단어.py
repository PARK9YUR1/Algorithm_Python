# 1411

N = int(input())
words = []

for _ in range(N):
    word = input()
    used = {}
    check = 0
    new_word = ''

    for w in word:
        if w in used:
            new_word += str(used[w])
        else:
            check += 1
            used[w] = check
            new_word += str(used[w])

    words.append(new_word)

result = 0

for i in range(N):
    for j in range(i+1, N):
        if words[i] == words[j]:
            result += 1

print(result)