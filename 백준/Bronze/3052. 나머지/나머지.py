numbers = []
for i in range(10) :
    i = int(input())
    numbers.append(i)

number_42 = []
for i in numbers :
    j = i % 42
    number_42.append(j)

print(len(set(number_42)))