N = int(input())

for i in range(N):
    blank = N - i - 1
    print(" " * blank, end='')
    print("* " * i, end='')
    print("*")