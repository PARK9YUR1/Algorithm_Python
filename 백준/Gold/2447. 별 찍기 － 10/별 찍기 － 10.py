import sys
input = sys.stdin.readline

def star(x):
    if x == 3:
        arr = ['***', '* *', '***']
        return arr
    else:
        new_x = x // 3
        s = star(new_x)
        arr = [[] for _ in range(x)]
        for i in range(x):
            if i//new_x == 1:
                arr[i] = s[i%new_x] + " "*new_x + s[i%new_x]
            else:
                arr[i] = s[i%new_x]*3
        return arr

N = int(input().rstrip())
result = star(N)
for res in result:
    print(res)