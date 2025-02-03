import sys
sys.setrecursionlimit(10**6)


def solution(l, r):
    
    result = []
    
    def dfs(num):
        
        if num > r:
            return
        
        if l <= num <= r:
            result.append(num)
        
        dfs(num * 10 + 0)
        dfs(num * 10 + 5)
        
    dfs(5)
    
    return sorted(result) if result else [-1]
