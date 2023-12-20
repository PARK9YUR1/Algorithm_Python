def solution(m, musicinfos):
    # 네오가 들은 음악
    neo = []
    i, N = 0, len(m)
    while i < N:
        if i < N-1:
            if m[i+1] == '#':
                neo.append(m[i:i+2])
                i += 2
            else:
                neo.append(m[i])
                i += 1
        else:
            neo.append(m[i])
            i += 1
    
    result = []  # 조건이 일치하는 음악 담을 배열
    
    for idx in range(len(musicinfos)):
        start, end, name, musics = musicinfos[idx].split(',')
        
        # idx번째 음악
        music = []
        i, N = 0, len(musics)
        while i < N:
            if i < N-1:
                if musics[i+1] == '#':
                    music.append(musics[i:i+2])
                    i += 2
                else:
                    music.append(musics[i])
                    i += 1
            else:
                music.append(musics[i])
                i += 1
        
        # 재생시간 계산
        start = int(start[:2])*60 + int(start[3:])
        end = int(end[:2])*60 + int(end[3:])
        time = end - start
        
        # 재생된 음악 구하기
        l = len(music)  # 음악길이
        if time > l:  # 재생시간이 음악길이보다 긴 경우
            x = time // l
            y = time % l
            play_music = music * x + music[:y]
        else:         # 아닌 경우
            play_music = music[:time]
        
        # 네오가 들은 음악과 재생된 음악 비교
        n, p = ' '.join(neo)+' ', ' '.join(play_music)+' '
        if n in p:  # 조건일치하면 result 배열에 추가
            result.append([time, idx, name])
            # print(f'name {name} / neo {n} / play_music {p}')
        
    if result:
        result.sort(key=lambda x:(-x[0], x[1]))  # 재생시간순, 입력순 정렬
        answer = result[0][2]
    else:
        answer = '(None)'
        
    return answer