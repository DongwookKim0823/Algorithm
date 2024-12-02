def solution(mats, park):
    
    def check_range(i, j):
                
        increase = 0
        while True:
            if i + increase >= len(park) or j + increase >= len(park[0]):
                return increase
                
            for k in range(increase + 1):
                if park[i + k][j + increase] != '-1' or park[i + increase][j + k] != '-1':
                    return increase

            increase += 1
            
            
    max_area = float('-inf')
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == '-1':
                max_area = max(check_range(i, j), max_area)
    
    for i in sorted(mats, reverse=True):
        if i <= max_area:
            return i
        
    return -1
