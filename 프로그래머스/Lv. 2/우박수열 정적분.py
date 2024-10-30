def solution(k, ranges):
    
    calc_list = [k]
    while k > 1:
        k = k // 2 if k % 2 == 0 else k * 3 + 1
        calc_list.append(k)
        
    area_list = [(calc_list[i] + calc_list[i + 1]) / 2 for i in range(len(calc_list) - 1)]

    answer = []
    n = len(calc_list) - 1
    for start, end in ranges:
        end = end if end > 0 else n + end
             
        if start > end:
            answer.append(-1.0)
        elif start == end:
            answer.append(0.0)
        else:
            answer.append(sum(area_list[start:end]))
        
    return answer
