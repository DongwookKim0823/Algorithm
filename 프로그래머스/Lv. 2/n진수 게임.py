def solution(n, t, m, p):
    
    num_list = '0123456789ABCDEF'
    
    num_string = ''
    for i in range(0, t * m):
        
        temp = ''
        while True:
            temp =  num_list[i % n] + temp
            i //= n
            if i < n:
                if i != 0:
                    temp = num_list[i] + temp
                break
                
        num_string += temp
        if len(num_string) > t * m:
            break
    
    answer = ''
    for index in range(p - 1, t * m, m):
        answer += num_string[index]
    
    return answer
