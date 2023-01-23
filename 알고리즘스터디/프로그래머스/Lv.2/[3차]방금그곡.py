def solution(m, musicinfos):
    answer = ''
    
    musics = []
    m = m.replace('C#', 'V')
    m = m.replace('D#', 'Z')
    m = m.replace('F#', 'Y')
    m = m.replace('G#', 'W')
    m = m.replace('A#', 'X')  
    for i in range(len(musicinfos)):
        temp = []
        a, b = map(int, musicinfos[i].split(',')[0].split(':'))
        c, d = map(int, musicinfos[i].split(',')[1].split(':'))
        time = -a*60 - b + c*60 + d
        melody = musicinfos[i].split(',')[3]
        melody = melody.replace('C#', 'V')
        melody = melody.replace('D#', 'Z')
        melody = melody.replace('F#', 'Y')
        melody = melody.replace('G#', 'W')
        melody = melody.replace('A#', 'X')
        temp.append(time)
        temp.append(musicinfos[i].split(',')[2])
        temp_music = ''
        for a in range(time):
            temp_music += melody[a%len(melody)]
        temp.append(temp_music)
        musics.append(temp)
    
    ans_list = []
    max_time = 1
    for music in musics:
        if m in music[2]:
            ans_list.append([music[0], music[1]])
            if music[0] >= max_time:
                max_time = music[0]
    
    for time, ans in ans_list:
        if time == max_time:
            answer = ans
            break
            
    if ans_list == []:
        answer = "(None)"
        
    return answer