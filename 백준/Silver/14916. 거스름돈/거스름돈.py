N = int(input())
if N < 5:
    if N%2 == 0:
        print(N//2)
    else:
        print(-1)
else:
    if N%5 == 0:
        print(N//5)
    else:
        a = N - (N//5)*5
        b = N - (N//5 - 1)*5
        if a % 2 == 0:
            print(N//5 + a//2)
        else:
            if b%2 == 0:
                print(N//5 - 1 + b//2)
            else:
                print(-1)