from collections import deque

def solution(maps):
    
    def bfs(start_i, start_j):
        queue = deque([(start_i, start_j)])
        visited[start_i][start_j] = True
        days = int(maps[start_i][start_j])
        
        while queue:
            cur_y, cur_x = queue.popleft()
                
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ny, nx = cur_y + dy, cur_x + dx
                
                if (0 <= nx < x and 0 <= ny < y) and not visited[ny][nx] and maps[ny][nx].isdigit():
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    days += int(maps[ny][nx])
                    
        return days

    
    y, x = len(maps), len(maps[0])
    visited = [[False] * x for _ in range(y)]
    answer = []
    
    for i in range(y):
        for j in range(x):
            if maps[i][j].isdigit() and not visited[i][j]:
                answer.append(bfs(i, j))

    return sorted(answer) if answer else [-1]
