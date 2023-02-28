def solution(survey, choices):
    
    answer = ''
    score = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    for element, choice in zip(survey, choices):
        if choice == 4: continue
        if choice // 4 == 0: score[element[choice // 4]] += 4 - choice % 4
        if choice // 4 == 1: score[element[choice // 4]] += choice % 4
        
    for element in ['RT', 'CF', 'JM', 'AN']:
        if score[element[0]] == score[element[1]]:
            answer += element[0]
        if score[element[0]] > score[element[1]]:
            answer += element[0]
        if score[element[0]] < score[element[1]]:
            answer += element[1]
    
    return answer