from collections import Counter

def solution(N, stages):
    
    rate_list = []
    user_count = Counter(stages)
    
    left_user = len(stages)
    for stage in range(1, N + 1):
        stage_user = user_count[stage]
        if stage_user == 0: failed_rate = 0
        else: failed_rate = stage_user / left_user
        rate_list.append((stage, failed_rate))
        left_user -= stage_user
    
    rate_list.sort(key = lambda x : (-x[1], x[0]))
    
    return [i[0] for i in rate_list]