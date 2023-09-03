alpha = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':2, 'H':3, 'I':3, 'J':2, 'K':2, 'L':1, 'M':2,
         'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1}

A, B = input(), input()
length = len(A) + len(B)
name = [[]]
for i in range(len(A)):
    name[0].append(alpha[A[i]])
    name[0].append(alpha[B[i]])
name += [[0] * i for i in range(length-1, 1, -1)]

for i in range(1, length-1):
    N = length-i
    for j in range(N):
        name[i][j] = (name[i-1][j] + name[i-1][j+1]) % 10

result = name[-1][0] * 10 + name[-1][1]
print('%02d' % result)