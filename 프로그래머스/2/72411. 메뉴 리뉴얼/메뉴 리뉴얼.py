from itertools import combinations

def solution(orders, courses):
    answer = []
    
    foods = []
    orders.sort(key=lambda x:len(x))
    for order in orders:
        food = [o for o in order]
        food.sort()
        foods.append(food)
    
    for course in courses:
        comb = {}
        for food in foods:
            if len(food) >= course:
                arr = list(combinations(food, course))
                for a in arr:
                    if a in comb:
                        comb[a] +=1
                    else:
                        comb[a] = 1
        
        if comb:
            mx = max(comb.values())
            mxs = [''.join(k) for k, v in comb.items() if v == mx and v != 1]
            answer += mxs
        
    answer.sort()
    return answer