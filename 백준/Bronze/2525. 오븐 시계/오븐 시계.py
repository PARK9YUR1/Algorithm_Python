A, B = map(int, input().split())
C = int(input())

if B+C < 60 :
    B += C
    print(f'{A} {B}')
else :
    X = (B+C)//60
    A += X
    B = (B+C)%60
    if A >= 24 : 
        A -= 24 
    print(f'{A} {B}')
    