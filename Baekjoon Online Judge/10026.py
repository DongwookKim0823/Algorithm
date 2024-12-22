import sys
from collections import deque

input = sys.stdin.readline


def bfs(i, j, field, visited):
    
    queue = deque([(i, j)])
    cur_color = field[i][j]
    visited.add((i, j))
    
    while queue:
        y, x = queue.popleft()
        
        for dx, dy in [(1 ,0), (0, -1), (-1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(field) and 0 <= ny < len(field) and (ny, nx) not in visited and cur_color == field[ny][nx]:
                queue.append((ny, nx))
                visited.add((ny, nx))


def check_status(length, field):
    
    visited = set()
    
    count = 0
    for i in range(length):
        for j in range(length):
            if (i, j) not in visited:
                bfs(i, j, field, visited)
                count += 1
        
        if len(visited) == length ** 2:
            break
        
    return count
            

if __name__ == '__main__':
    
    length = int(input())
    field = [list(input().rstrip()) for _ in range(length)]
        
    a = check_status(length, field)
    field = [['G' if element == 'R' else element for element in row] for row in field]    
    b = check_status(length, field)
    
    print(a, b)
