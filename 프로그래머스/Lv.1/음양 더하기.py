def solution(absolutes, signs):
    
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] is True else absolutes[i] * -1
            
    return answer