def solution(m, musicinfos):
    
    def standardize(melody):
        melody = melody.replace('C#', 'c')
        melody = melody.replace('D#', 'd')
        melody = melody.replace('F#', 'f')
        melody = melody.replace('G#', 'g')
        melody = melody.replace('A#', 'a')
        melody = melody.replace('B#', 'b')
        return melody
    
    def calculate_music_length(start_time, end_time):
        st_hour, st_minute = map(int, start_time.split(':'))
        ed_hour, ed_minute = map(int, end_time.split(':'))
        return (ed_hour * 60 + ed_minute) - (st_hour * 60 + st_minute)
    
    m = standardize(m)
    cand_list = []
        
    for idx, info in enumerate(musicinfos):
        start_time, end_time, name, sheet = info.split(',')
        music_len = calculate_music_length(start_time, end_time)
        sheet = standardize(sheet)

        index = 0
        full_music = ''
        for _ in range(music_len):
            full_music += sheet[index]
            index = (index + 1) % len(sheet)
            
        if m in full_music:
            cand_list.append((name, music_len, idx))
            
    if not cand_list:
        return "(None)"
    
    cand_list.sort(key=lambda x: (-x[1], x[2]))
        
    return cand_list[0][0]
    
