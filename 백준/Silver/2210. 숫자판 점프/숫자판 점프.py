arr = [list(map(str, input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
nums = set()

def dfs(x, y, depth, num):
    global nums
    if depth == 6:
        nums.add(num)
        return

    visited[x][y] = False

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, num + arr[nx][ny])
            visited[nx][ny] = False

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, arr[i][j])

print(len(nums))