def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')
    parsed_sets = [list(map(int, x.split(','))) for x in s]
    parsed_sets.sort(key=len)
    
    answer = []
    for element in parsed_sets:
        for num in element:
            if num not in answer:
                answer.append(num)
    
    return answer
