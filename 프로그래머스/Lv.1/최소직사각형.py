def solution(sizes):
    
    answer = [0, 0]
    for size in sizes:
        size.sort()
        if size[0] > answer[0]: answer[0] = size[0]
        if size[1] > answer[1]: answer[1] = size[1]
        
    return answer[0] * answer[1]