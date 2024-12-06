def solution(targets):
    
    targets.sort(key=lambda x: x[1])
    
    count = 0
    current_end = -1
    for s, e in targets:
        
        if current_end <= s:
            current_end = e
            count += 1
        
    return count
