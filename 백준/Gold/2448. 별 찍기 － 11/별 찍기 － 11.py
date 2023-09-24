import sys
input = sys.stdin.readline

def star(x):
    if x == 3:
        arr = ['  *  ', ' * * ', '*****']
        return arr
    else:
        s = star(x//2)
        arr = [' '*(x//2)+s[i]+' '*(x//2) for i in range(len(s))]
        arr2 = [s[i]+' '+s[i] for i in range(len(s))]
        return arr + arr2

N = int(input())
result = star(N)
for res in result:
    print(res)