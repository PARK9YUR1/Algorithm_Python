N = int(input())

def star(x):
    if x == 1:
        return ['*']
    else:
        arr = star(x-1)
        stars = ['*' * (4*x - 3), '*' + ' '*(4*x - 5) + '*']
        for i in range(len(arr)//2+1):
            stars.append('* ' + arr[i] + ' *')
        n = len(stars) - 1
        tmp = stars[:n]
        stars += tmp[::-1]
        return stars

result = star(N)
for res in result:
    print(res)