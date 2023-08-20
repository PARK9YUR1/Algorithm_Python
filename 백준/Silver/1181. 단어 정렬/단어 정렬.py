N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=len)

for w in words:
    print(w)
