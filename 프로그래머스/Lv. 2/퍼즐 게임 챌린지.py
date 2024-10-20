def solution(diffs, times, limit):
    
    def count_time(diffs, times, level):
        total_time = 0
        for index, diff in enumerate(diffs):
            if diff <= level:
                total_time += times[index]
            else:
                time_pre, time_cur = (0, times[index]) if index == 0 else (times[index - 1], times[index]) 
                total_time += (time_pre + time_cur) * (diff - level) + time_cur
                
        return total_time
            
        
    left = min(diffs)
    right = max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        if count_time(diffs, times, mid) > limit:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
