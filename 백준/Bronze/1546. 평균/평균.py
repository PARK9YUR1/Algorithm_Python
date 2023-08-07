N = int(input())
test = list(map(int, input().split()))

max_score = max(test)

new_test = []
for score in test :
    new_test.append(score/max_score*100)

avg = sum(new_test) / len(test)
print(avg)