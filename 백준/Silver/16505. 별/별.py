N = int(input())

stars = ['*']
for i in range(N):
    stars *= 2
    for j in range(len(stars)):
        if j < len(stars) // 2:
            stars[j] *= 2
        else:
            stars[j] += ' ' * (len(stars) - len(stars[j]))

for star in stars:
    print(star.rstrip())