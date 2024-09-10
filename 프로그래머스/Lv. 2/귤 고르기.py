from collections import defaultdict

def solution(k, tangerine):
    tangerine_dict = defaultdict(int)
    for element in tangerine:
        tangerine_dict[element] += 1
        
    count = 0
    tangerine_tuple = sorted(tangerine_dict.items(), key=lambda x: x[1], reverse=True)
    for key, value in tangerine_tuple:
        k -= value
        count += 1
        
        if k <= 0:
            break
        
    return count
