A, B = map(int, input().split())
str_A = str(A)
str_B = str(B)

reverse_str_A = str_A[::-1]
reverse_str_B = str_B[::-1]

reverse_A = int(reverse_str_A)
reverse_B = int(reverse_str_B)

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)