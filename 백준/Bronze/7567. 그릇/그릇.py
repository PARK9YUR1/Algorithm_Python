dishes = input()

before = dishes[0]
result = 10

for i in range(1, len(dishes)):
    dish = dishes[i]
    if before == dish:
        result += 5
    else:
        result += 10
    before = dish
print(result)