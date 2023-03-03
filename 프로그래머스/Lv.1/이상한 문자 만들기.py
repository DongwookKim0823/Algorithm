def solution(s):
    
    answer = ''
    for i in s.split(' '):
        if i == '':
            answer += ' '
            continue
        
        temp = ' '
        for j in range(len(i)):
            if j % 2 == 0: temp += i[j].upper()
            if j % 2 == 1: temp += i[j].lower()
        answer += temp
    
    return answer[1:]