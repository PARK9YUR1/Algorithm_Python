def zero(x, ans, arr):
    global result
    if x == N+1:
        txt = ''.join(arr)
        f = txt.replace(' ','')
        pm = 0  # 0 -> +  /  1 -> -
        total = 0
        str_num = ''
        for i in range(len(f)):
            if f[i].isdigit():
                str_num += f[i]
            else:
                num = int(str_num)
                str_num = ''
                if pm == 0:
                    total += num
                else:
                    total -= num
                if f[i] == '+':
                    pm = 0
                else:
                    pm = 1
            if i == len(f)-1:
                num = int(str_num)
                str_num = ''
                if pm == 0:
                    total += num
                else:
                    total -= num
        if total == 0:
            print(txt)
        return

    zero(x+1, ans, arr+[' ', str(x)])
    plus_minus[x][0] = 1
    zero(x+1, ans+x, arr+['+', str(x)])
    plus_minus[x][0] = 0
    plus_minus[x][1] = 1
    zero(x+1, ans-x, arr+['-', str(x)])
    plus_minus[x][1] = 0

tc = int(input())
for _ in range(tc):
    N = int(input())
    plus_minus = [[0,0]]*(N+1)
    zero(2, 0, ['1'])
    print()
