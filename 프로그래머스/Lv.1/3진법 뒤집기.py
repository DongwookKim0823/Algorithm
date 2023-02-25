def solution(n):
    temp = ''
    while n:
        temp = str(n % 3) + temp
        n = n // 3
        
    answer = 0    
    for i, j in enumerate(temp):
        answer += 3 ** i * int(j)
        
    return answer