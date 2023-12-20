def solution(m, musicinfos):
    neo = []  # 네오가 들은 음악
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
    
    result = []
    
    for idx in range(len(musicinfos)):
        start, end, name, musics = musicinfos[idx].split(',')
        
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
        
        start = int(start[:2])*60 + int(start[3:])
        end = int(end[:2])*60 + int(end[3:])
        time = end - start
        l = len(music)
        
        if time > l:
            x = time // l
            y = time % l
            play_music = music * x + music[:y]
        else:
            play_music = music[:time]
            
        n, p = ' '.join(neo)+' ', ' '.join(play_music)+' '
        if n in p:
            result.append([time, idx, name])
            print(f'name {name} / neo {n} / play_music {p}')
            # print(name, neo, play_music)
        
        # print(''.join(play_music))
        
    if result:
        result.sort(key=lambda x:(-x[0], x[1]))
        answer = result[0][2]
    else:
        answer = '(None)'
    return answer