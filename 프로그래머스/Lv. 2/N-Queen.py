def solution(n):
    
    def check_possible(row, col, queen_state):
        
        for element_row, element_col in queen_state:
            
            if element_col == col:
                return False
            
            if element_row - row == element_col - col:
                return False
            
            if element_row + element_col == row + col:
                return False
            
        return True
            
        
    count = 0
    def recursive_func(row, queen_state):
        
        if row >= n:
            
            if len(queen_state) == n:
                nonlocal count
                count += 1
                
            return
        
        for i in range(1, n + 1):
            if check_possible(row + 1, i, queen_state):
                recursive_func(row + 1, queen_state + [(row + 1, i)])
        
    for i in range(1, n + 1):
        recursive_func(1, [(1, i)])
    
    return count
