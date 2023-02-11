from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    dist = [[-1] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    queue = deque()
    queue.append(0)
    queue.append(0)
    dist[0][0] = 1
    visit[0][0] = True
    
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            
            if nx >= N  or nx < 0  or ny < 0 or ny >= M: continue
            if maps[nx][ny] == 0: continue
            if visit[nx][ny] == True: continue
            
            dist[nx][ny] = 1 + dist[x][y]
            visit[nx][ny] = True
            queue.append(nx)
            queue.append(ny)
            
    if dist[N-1][M-1] == 0:
        answer = -1
    else:
        answer = dist[N-1][M-1]

    return answer