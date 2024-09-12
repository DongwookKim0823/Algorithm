def calculate_sec(time):
    time_min, time_sec = map(int, time.split(':'))
    return time_min * 60 + time_sec

def solution(video_len, pos, op_start, op_end, commands):
    video_total_sec = calculate_sec(video_len)
    cur_total_sec = calculate_sec(pos)
    op_start_sec = calculate_sec(op_start)
    op_end_sec = calculate_sec(op_end)
    
    def move_next(cur_total_sec):
        cur_total_sec += 10
        if cur_total_sec >= video_total_sec:
            return video_total_sec
        return cur_total_sec
        
    def move_prev(cur_total_sec):
        cur_total_sec -= 10
        if cur_total_sec <= 0:
            return 0
        return cur_total_sec
    
    if op_start_sec <= cur_total_sec <= op_end_sec:
        cur_total_sec = op_end_sec
    
    for command in commands:
        if command == "next":
            cur_total_sec = move_next(cur_total_sec)
        else:
            cur_total_sec = move_prev(cur_total_sec)
            
        if op_start_sec <= cur_total_sec <= op_end_sec:
            cur_total_sec = op_end_sec
            
    result_min = cur_total_sec // 60
    result_sec = cur_total_sec % 60
    
    return f"{result_min:02}:{result_sec:02}"
