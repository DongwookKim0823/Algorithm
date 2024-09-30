import math

def solution(k, r):
    
    answer = 0
    for x in range(0, r + 1, k):
        max_y = math.floor(math.sqrt(r**2 - x**2))
        answer += (max_y // k + 1)
    
    return answer
