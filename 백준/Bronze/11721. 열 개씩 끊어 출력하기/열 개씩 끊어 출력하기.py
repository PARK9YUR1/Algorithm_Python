txt = input()
length = len(txt)//10
for i in range(1, length+2):
    x = i * 10
    print(txt[x-10:x])