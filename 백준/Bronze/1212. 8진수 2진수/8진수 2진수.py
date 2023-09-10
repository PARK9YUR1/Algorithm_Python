num_8 = '0o' + input()
num = int(num_8, 8)
i = 2
result = bin(num)
if num_8 != '0o0':
    for j in range(len(result)):
        if result[j] == '1':
            i = j
            break
result = bin(num)[i:]
print(result)