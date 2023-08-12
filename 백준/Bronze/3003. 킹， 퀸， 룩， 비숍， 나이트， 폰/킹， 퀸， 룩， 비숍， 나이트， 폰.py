N = list(map(int, input().split()))
chess_list = [1, 1, 2, 2, 2, 8]

for i in range(len(N)):
    print(chess_list[i] - N[i], end = ' ')