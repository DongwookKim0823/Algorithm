from collections import deque

def solution(x, y, n):
    
    def bfs():
        visited = set()
        
        queue = deque([(x, 0)])
        visited.add(x)
        
        while queue:
            
            cur_x, count = queue.popleft()
            
            if cur_x == y:
                return count
            
            for next_x in [cur_x + n,  cur_x * 2, cur_x * 3]:
                if next_x not in visited and next_x <= y:
                    queue.append((next_x, count + 1))
                    visited.add(next_x)
                    
        return -1

    return bfs()
