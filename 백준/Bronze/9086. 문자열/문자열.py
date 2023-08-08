T = int(input()) # test case

for i in range(T) :
    word = str(input())
    print(f'{word[0]}{word[len(word)-1]}')