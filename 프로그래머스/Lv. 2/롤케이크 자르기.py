from collections import Counter, defaultdict


def solution(topping):
    remaining_topping_dict = Counter(topping)
    moved_topping_dict = defaultdict(int)
    
    count = 0
    for element in topping:
        if remaining_topping_dict[element] == 1:
            del remaining_topping_dict[element]
        else:
            remaining_topping_dict[element] -= 1
            
        moved_topping_dict[element] += 1
        
        if len(remaining_topping_dict) == len(moved_topping_dict):
            count += 1
            
    return count
