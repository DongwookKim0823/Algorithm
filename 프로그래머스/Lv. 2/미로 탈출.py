from collections import deque


def solution(maps):
    
    def bfs(start, target):
        
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        
        queue = deque([[start, 0]])
        visited[start[0]][start[1]] = True

        while queue:
            
            cur_point, count = queue.popleft()
            
            if cur_point == target:
                return count
            
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                ny, nx = dy + cur_point[0], dx + cur_point[1]
                
                if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and not visited[ny][nx] and maps[ny][nx] != 'X':
                    queue.append(((ny, nx), count + 1))
                    visited[ny][nx] = True
                    
        
        return -1
        
    
    start = ()
    end = ()
    lever = ()
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            if maps[i][j] == 'E':
                end = (i, j)
            if maps[i][j] == 'L':
                lever = (i, j)
    
    to_lever = bfs(start, lever)
    to_end = bfs(lever, end)

    return to_lever + to_end if to_lever != -1 and to_end != -1 else -1
