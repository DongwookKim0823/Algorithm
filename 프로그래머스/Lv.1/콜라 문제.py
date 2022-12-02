def solution(a, b, n):
    
    answer = 0
    while True:
        get_cnt, remain_cnt = (n // a) * b, n % a
        if get_cnt == 0: break
        answer += get_cnt
        n = get_cnt + remain_cnt
    return answer