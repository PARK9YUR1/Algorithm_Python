txt = input()
result = txt[0]
for i in range(1, len(txt)):
    if txt[i] == '-':
        result += txt[i+1]
print(result)