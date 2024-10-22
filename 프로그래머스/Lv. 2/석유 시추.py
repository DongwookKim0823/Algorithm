from collections import deque, defaultdict

def solution(land):
    
    def bfs(start, visited):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        
        area = 1
        points = [start]
        while queue:
            cur_y, cur_x = queue.popleft()
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = cur_x + dx, cur_y + dy
                
                if 0 <= nx < len(land[0]) and 0 <= ny < len(land) and not visited[ny][nx] and land[ny][nx] == 1:
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    
                    area += 1
                    points.append((ny, nx))
                    
        return area, points
            

    area_dict = defaultdict(int)
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and not visited[i][j]:
                area, points = bfs((i, j), visited)
                
                for col in set(point[1] for point in points):
                    area_dict[col] += area
                    
    return max(area_dict.values())
