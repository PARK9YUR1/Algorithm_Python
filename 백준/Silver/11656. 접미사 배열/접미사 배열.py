S = input()
words = []
n = len(S)

for i in range(n):
    words.append(S[i:])
words.sort()

for word in words:
    print(word)