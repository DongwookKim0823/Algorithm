def solution(n):
    answer = [[0] * n for _ in range(n)]
    for index in range(n):
        answer[index][index] = 1
        
    return answer
