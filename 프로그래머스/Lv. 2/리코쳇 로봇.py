from collections import deque


def solution(board):
    
    def bfs(start):     
        visited = set()
        
        queue = deque([[start, 0]])
        visited.add(start)
        while queue:
            start, count = queue.popleft()
            
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx, ny = start[1], start[0]
                while 0 <= nx + dx < len(board[0]) and 0 <= ny + dy < len(board) and board[ny + dy][nx + dx] != 'D':
                    nx += dx
                    ny += dy
                                        
                if board[ny][nx] == 'G':
                    return count + 1
                
                if (ny, nx) not in visited:
                    queue.append([(ny, nx), count + 1])
                    visited.add((ny, nx))
    
        return -1

    start = ()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
        
    return bfs(start)
