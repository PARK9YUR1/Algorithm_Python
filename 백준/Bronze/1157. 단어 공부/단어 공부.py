word = str(input())
new_word = word.upper()
new_word_list = []

mx_cnt = 0
mx_cnt_s = ''

for s in new_word:
    new_word_list.append(s)

new_word_list = list(set(new_word_list))

for i in new_word_list:
    cnt = new_word.count(i)
    if cnt > mx_cnt:
        mx_cnt = new_word.count(i)
        mx_cnt_s = i
    elif cnt == mx_cnt:
        mx_cnt = new_word.count(i)
        mx_cnt_s = '?'

print(mx_cnt_s)