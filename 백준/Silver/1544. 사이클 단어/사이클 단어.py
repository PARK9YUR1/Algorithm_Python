N = int(input())
words = []
cnt = 0
for _ in range(N):
    word = input()
    if word not in words:
        cnt += 1
        for n in range(len(word)):
            x = word[n:] + word[:n]
            if x not in words:
                words.append(x)

print(cnt)