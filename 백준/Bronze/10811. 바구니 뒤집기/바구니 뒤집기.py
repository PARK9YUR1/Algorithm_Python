N, M = map(int, input().split())
N_list = []

for n in range(N) :
    N_list.append(n+1)

for num in range(M) :
    i, j = map(int, input().split())
    for num2 in range(i, j) :
        if i > j :
            continue
        while True :
            tmp = N_list[i-1]
            N_list[i-1] = N_list[j-1]
            N_list[j-1] = tmp
            i += 1
            j -= 1
            if i >= j :
                break

for x in N_list :
    print(x, end = ' ')