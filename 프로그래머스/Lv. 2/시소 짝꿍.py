from collections import Counter

def solution(weights):
    weight_counter = Counter(weights)
    
    count = 0
    for weight in sorted(weight_counter):
        if weight_counter[weight] > 1:
            count += weight_counter[weight] * (weight_counter[weight] - 1) // 2
            
        for ratio in [4/3, 4/2, 3/2]:
            count += weight_counter[weight] * weight_counter[weight * ratio]
            
    return count
