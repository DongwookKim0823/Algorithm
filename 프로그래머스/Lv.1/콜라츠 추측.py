def solution(num):
    
    if num == 1: return 0

    cnt = 0
    while num != 1:
        if cnt > 500: return -1
        
        cnt += 1
        if num % 2 == 0:
            num = num // 2
            continue
        if num % 2 == 1:
            num = num * 3 + 1
            continue
            
    return cnt