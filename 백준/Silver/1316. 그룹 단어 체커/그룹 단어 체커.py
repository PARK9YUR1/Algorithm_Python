N = int(input())  # 단어개수
cnt = 0

for n in range(N):
    group_word = True
    word = input()
    word += '0'

    check_list = []
    for i in range(len(word)-1):
        # 체크리스트에 알파벳 넣기 (이미 있을경우 x)
        if word[i] not in check_list:
            check_list.append(word[i])
        # i와 i+1 알파벳이 다른데 체크리스트에 i+1 있는 경우(앞에서 나온 문자일 경우)
        if word[i] != word[i+1] and word[i+1] in check_list:
            group_word = False
    if group_word == True:  # 그룹단어 맞으면 cnt + 1
        cnt += 1

print(cnt)