def solution(dartResult):
    
    games = []
    temp = dartResult[0]
    for i in dartResult[1:]:
        if i.isdigit() == True:
            if i == '0' and temp == '1':
                temp += i
            else:
                games.append(temp)
                temp = i
        else:
            temp += i
    games.append(temp)
    ######################## 게임별 문자열 분리########################
    
    answers = []
    for i, game in enumerate(games):
        answer = 0
        for element in game:
            if element.isdigit():
                if element == '0':
                    if answer != 0:
                        answer = 10
                answer += int(element)
            if element == 'S': answer = answer ** 1
            if element == 'D': answer = answer ** 2
            if element == 'T': answer = answer ** 3
            if element == '*':
                if i == 0:
                    answer *= 2
                else:
                    answer *= 2
                    answers[i - 1] *= 2
            if element == '#':
                 answer *= -1
        answers.append(answer)
        
    return sum(answers)