from collections import defaultdict

def solution(msg):
    
    alpha_dict = {k : v for k, v in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27))}
    
    answer = []
    temp_str = ''
    
    start, end = 0, 1
    while True:
        
        if msg[start:end] in alpha_dict:
            temp_str = alpha_dict[msg[start:end]]
            end += 1
        else:
            answer.append(temp_str)
            temp_str = ''
            alpha_dict[msg[start:end]] = max(alpha_dict.values()) + 1
            start, end = end - 1, end
            
        if end >= len(msg) + 1:
            answer.append(temp_str)
            break
        
    return answer
