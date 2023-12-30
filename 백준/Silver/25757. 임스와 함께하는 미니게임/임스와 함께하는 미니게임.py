N, game = input().split()
players = set()

for _ in range(int(N)):
    player = input()
    players.add(player)

if game == 'Y':
    print(len(players))
elif game == 'F':
    print(len(players)//2)
elif game == 'O':
    print(len(players)//3)