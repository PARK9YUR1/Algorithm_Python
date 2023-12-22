# 97-122 65-90
word = input()
result = ''
for w in word:
    num = ord(w)
    if 97 <= num <= 122:
        result += chr(num-32)
    else:
        result += chr(num+32)
print(result)