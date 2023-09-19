import sys
input = sys.stdin.readline

def N_Queen(N):
    def check(r, c):
        for i in range(r):
            if abs(i - r) == abs(board[i] - c):
                return False
        return True

    def queen(r):
        nonlocal cnt
        if r == N:
            cnt += 1
            return

        for c in range(N):
            if visited[c] == False and check(r, c) == True:
                board[r] = c
                visited[c] = True
                queen(r + 1)
                visited[c] = False

    cnt = 0
    board = [-1] * N
    visited = [False] * N
    queen(0)
    return cnt

N = int(input())
cnt = N_Queen(N)
print(cnt)

