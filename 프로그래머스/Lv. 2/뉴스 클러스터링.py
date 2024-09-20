import re
from collections import defaultdict

def solution(str1, str2):
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_dict[str1[i].lower() + str1[i + 1].lower()] += 1
            
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_dict[str2[i].lower() + str2[i + 1].lower()] += 1
            
    if not (str1_dict or str2_dict):
        return 65536
    
    intersection = 0
    union = 0
    all_keys = set(str1_dict.keys()).union(set(str2_dict.keys()))
    
    for key in all_keys:
        intersection += min(str1_dict[key], str2_dict[key])
        union += max(str1_dict[key], str2_dict[key])

    return int(intersection / union * 65536)
    
