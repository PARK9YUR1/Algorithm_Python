H, M = map(int, input().split())

if M >= 45 and M < 60 :
    M -= 45
    print(f'{H} {M}')
else : 
    M += 15
    if H != 0 :
        H -= 1
    else : 
        H = 23
    print(f'{H} {M}')