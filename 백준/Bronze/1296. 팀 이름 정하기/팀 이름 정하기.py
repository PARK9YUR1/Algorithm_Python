def check_LOVE(name):
    global L, O, V, E
    L += name.count('L')
    O += name.count('O')
    V += name.count('V')
    E += name.count('E')

def calc():
    ans = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    return ans

yd_name = input()
N = int(input())
team = {}
for _ in range(N):
    L, O, V, E = 0, 0, 0, 0
    team_name = input()
    check_LOVE(yd_name)
    check_LOVE(team_name)
    team[team_name] = calc()

sorted_team = dict(sorted(team.items(), key=lambda x:(-x[1], x[0])))
print(list(sorted_team.keys())[0])
