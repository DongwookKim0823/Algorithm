from collections import deque

def bfs(field, n, m):
    queue = deque([(0, 0, 1)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        y, x, count = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return count
        
        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == '1' and not visited[ny][nx]:
                queue.append([ny, nx, count + 1])
                visited[ny][nx] = True


if __name__ == '__main__':
    n, m = map(int, input().split())

    field = []
    for _ in range(n):
        field.append(list(input()))
        
    print(bfs(field, n, m))
