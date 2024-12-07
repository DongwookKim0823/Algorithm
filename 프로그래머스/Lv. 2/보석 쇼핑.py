from collections import defaultdict


def solution(gems):
    
    gem_set = set(gems)
    gem_len = len(gems)
    current_dict = defaultdict(int)
    current_set = set()
    
    left, right = 0, 0
    candidate = []
    while right < gem_len:
        
        current_dict[gems[right]] += 1
        current_set.add(gems[right])
        
        left_move = False
        while len(current_set) == len(gem_set) and left < gem_len:
            current_dict[gems[left]] -= 1
            
            if current_dict[gems[left]] == 0:
                current_set.remove(gems[left])
                
            left += 1
            left_move = True
        
        if left_move:
            candidate = [left, right + 1] if candidate == [] or right + 1 - left < candidate[1] - candidate[0] else candidate
        
        right += 1
        
    return candidate
