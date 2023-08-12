N = int(input())

for i in range(2*N-1):
    if i < N:
        print(' '*(N-1-i), end='')
        print('*'*(2*i+1), end='')
        print()
    else:
        print(' '*(i-N+1), end='')
        print('*'*(2*(2*N-i)-3), end='')
        print()