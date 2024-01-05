def solution(n, words):
    answer = [0, 0]
    used = [words[0]]
    turn = 1
    
    prev = words[0][-1]
    for i in range(1, len(words)):
        if i % n == 0:
            turn += 1
        word = words[i]
        cur = word[0]

        if prev != cur or word in used:
            answer = [i%n + 1, turn]
            break
        else:
            used.append(word)
        prev = word[-1]

    return answer