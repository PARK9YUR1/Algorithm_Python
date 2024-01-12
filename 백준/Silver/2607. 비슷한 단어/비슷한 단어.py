# "GOD" - "DOG"
def func1(word):
    if word == first_word:
        return True
    else:
        return False

# "GOD" - "GOOD"
def func2(mx, mn):
    if len(word) == len(first_word):
        return False
    else:
        if len(mx) - len(mn) == 1:
            for i in range(len(mx)):
                x = mx.pop(i)
                if mx == mn:
                    mx.insert(i, x)
                    return True
                else:
                    mx.insert(i, x)
        return False

# "GOD" - "GOT"
def func3(word):
    if len(word) == len(first_word):
        w = []
        for i in range(len(first_word)):
            a = first_word[i]
            if a in word:
                idx = word.index(a)
                word.pop(idx)
                w.append(a)
        if len(word) == 1:
            return True
    return False


N = int(input())
first_word = list(input())
first_word.sort()

words = [list(input()) for _ in range(N-1)]

cnt = 0
for word in words:
    w = ''.join(word)
    word.sort()
    bool1 = func1(word)
    if len(word) > len(first_word):
        bool2 = func2(word, first_word)
    else:
        bool2 = func2(first_word, word)
    bool3 = func3(word)
    if bool1 or bool2 or bool3:
        cnt += 1

print(cnt)