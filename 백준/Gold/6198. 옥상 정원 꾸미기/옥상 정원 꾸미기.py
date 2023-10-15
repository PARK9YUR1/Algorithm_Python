N = int(input())  # 빌딩 개수
building = [int(input()) for _ in range(N)]
cnt = [0]*N  # i번째 빌팅옥상 확인할 수 있는 관리인 수
stack = []
for i in range(N):
    while stack:
        if stack[-1] > building[i]:
            break
        stack.pop()
    cnt[i] = len(stack)  # stack: i번째 빌딩옥상을 확인할 수 있는 관리인의 빌딩 높이
    stack.append(building[i])
print(sum(cnt))