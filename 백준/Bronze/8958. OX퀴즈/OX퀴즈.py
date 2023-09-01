N = int(input())
for _ in range(N):
    res = input()
    result = 0
    lst = [0] * len(res)

    if res[0] == 'O':
        lst[0] = 1
    for i in range(1, len(res)):
        if res[i] == 'O':
            lst[i] = lst[i-1] + 1
        else:
            lst[i] = 0

    print(sum(lst))