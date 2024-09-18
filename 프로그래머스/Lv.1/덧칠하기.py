def solution(n, m, section):
    count = 0
    i = 0
    
    while i < len(section):
        start = section[i]
        
        while i < len(section) and section[i] < start + m:
            i += 1
            
        count += 1
        
    return count
