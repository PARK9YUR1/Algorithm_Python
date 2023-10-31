N = int(input())

for i in range(N):
    blank1 = N - i - 1
    blank2 = 2 * i - 1
    if i == N-1:
        print("*"*(2*N-1))
    elif i == 0:
        print(" " * blank1, end='')
        print("*")
    else:
        print(" " * blank1, end='')
        print("*", end='')
        print(" " * blank2, end='')
        print("*")
