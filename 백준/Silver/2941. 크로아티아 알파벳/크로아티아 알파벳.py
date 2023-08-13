word = str(input())
word += '00'

cnt = 0
alpha = []
for a in range(97, 123):
    alpha.append(chr(a))
for i in range(len(word)-2):
    A = word[i:i + 3]
    B = word [i:i+2]
    C = word[i-1:i+2]
    D = word[i-1:i+1]
    if A=='dz=' or B=='c=' or B=='c-' or B=='d-' or B=='lj' or B=='nj' or B=='s=' or B=='z=':
        if B=='z=' and i-1 >= 0 and word[i-1] == 'd':
            continue
        cnt += 1
    if word[i] in alpha:
        if A=='dz=' or B=='c=' or B=='c-' or B=='d-' or B=='lj' or B=='nj' or B=='s=' or B=='z=':
            continue
        if i-1 != 0 and C=='dz=' or D=='lj' or D=='nj':
            continue
        cnt += 1

print(cnt)