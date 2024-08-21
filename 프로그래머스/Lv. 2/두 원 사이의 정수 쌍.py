import math

def solution(r1, r2):
    count = 0
    
    for x in range(0, r2 + 1):
        max_y = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        min_y = math.ceil(math.sqrt(r1 ** 2 - x ** 2)) if x**2 < r1**2 else 0
        
        count += (max_y - min_y + 1)
        
    return (count - (r2 - r1 + 1)) * 4
