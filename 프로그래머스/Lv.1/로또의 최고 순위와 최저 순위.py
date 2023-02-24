def solution(lottos, win_nums):
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_cnt = lottos.count(0)
    
    correct_cnt = 0
    for i in lottos:
        if i in win_nums:
            correct_cnt += 1
    
    return [rank[correct_cnt + zero_cnt], rank[correct_cnt]]