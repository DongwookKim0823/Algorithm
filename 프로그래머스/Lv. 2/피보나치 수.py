def solution(n):

    result = [0] * (n + 1)
    result[0] = 0
    result[1] = 1
    
    for index in range(2, n + 1):
        result[index] = (result[index - 1] + result[index - 2]) % 1234567
        
    return result[n]
