p, m = map(int, input().split())  # 플레이어 수, 방의 정원
players = [tuple(input().split()) for _ in range(p)]  # (레벨, 닉네임)
rooms = []

for player in players:
    level, nickname = int(player[0]), player[1]
    p = (level, nickname)
    enter = [room for room in rooms if rooms and room[0]-10 <= level <= room[0]+10 and len(room[1]) < m]

    # 입장 가능한 방이 있는 경우
    if enter:
        i = enter[0][2]
        rooms[i][1].append(p)

    # 없는 경우
    else:
        idx = len(rooms)
        rooms.append((level, [p], idx))


for room in rooms:
    room[1].sort(key=lambda x: x[1])
    
    if len(room[1]) == m:
        print('Started!')
        for player in room[1]:
            print(*player)
    else:
        print('Waiting!')
        for player in room[1]:
            print(*player)