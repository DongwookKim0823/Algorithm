from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    a, b = queue.popleft()
    
    for i in range(4): 
      if 0<=a+dx[i]<n and 0<=b+dy[i]<m:
         if graph[a+dx[i]][b+dy[i]] == 1:
           graph[a+dx[i]][b+dy[i]] = graph[a][b] + 1
           queue.append((a+dx[i],b+dy[i]))
  return graph[n-1][m-1]
   
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))