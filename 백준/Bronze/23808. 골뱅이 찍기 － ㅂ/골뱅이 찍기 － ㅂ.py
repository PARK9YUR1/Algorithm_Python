N = int(input())

arr1 = ['@', ' ', ' ', ' ', '@']
arr2 = ['@', '@', '@', '@', '@']

B = [arr1*N, arr1*N, arr2*N, arr1*N, arr2*N]
for i in range(5):
    for j in range(5*N):
        print(B[i][j]*N, end='')
        if j % 5 == 4:
            print()