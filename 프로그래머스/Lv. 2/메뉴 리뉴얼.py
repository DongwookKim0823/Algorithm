from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    
    new_course = []
    for amount in course:
        temp_dict = defaultdict(int)
        for order in orders:
            for cand in combinations(order, amount):
                temp_dict[''.join(sorted(cand))] += 1
                
        key_list = []
        cur_max_value = 0
        for key, value in temp_dict.items():
            
            if value >= 2:
                if cur_max_value < value:
                    key_list = [key]
                    cur_max_value = value
                    continue
                
                if cur_max_value == value:
                    key_list.append(key)
                    continue
        
        new_course.extend(key_list)
        
    new_course.sort()
    
    return new_course
