def solution(my_strings, parts):
    
    answer = ''
    for index, part in enumerate(parts):
        answer += my_strings[index][part[0]:part[1] + 1]

    return answer
