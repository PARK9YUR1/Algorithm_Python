word = input()
alpha = [0]*26
for w in word:
    i = ord(w) - 97
    alpha[i] += 1
print(*alpha)