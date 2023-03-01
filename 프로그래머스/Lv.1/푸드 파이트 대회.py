def solution(food):
    
    answer = ''
    for i in range(1, len(food)):
        if food[i] // 2 == 0:
            continue
        else:
            answer += str(i) * (food[i] // 2)
            
    answer += '0'
    
    for i in answer[-2::-1]: answer += i
        
    return answer