while True:
    txt = input()
    if txt == 'end':
        break
    txt = list(txt)
    word = ''.join(txt)

    check = True
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1] and txt[i] not in 'eo':
            check = False
            break

    cnt = 0
    for i in range(len(txt)):
        if txt[i] in 'aeiou':
            txt[i] = 0
            cnt += 1
        else:
            txt[i] = 1

    for i in range(len(txt)-2):
        if txt[i] == 0 and txt[i+1] == 0 and txt[i+2] == 0:
            check = False
            break
        elif txt[i] == 1 and txt[i+1] == 1 and txt[i+2] == 1:
            check = False
            break

    if check == True and cnt != 0:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')