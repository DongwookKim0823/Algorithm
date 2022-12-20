def solution(x):
    
    num = x
    sum_x = 0
    while num != 0:
        sum_x += num % 10
        num = num // 10

    return True if x % sum_x == 0 else False