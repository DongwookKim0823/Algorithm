def dfs(x, y):
  if 0<=x<n and 0<=y<m:
    if graph[x][y] == 0:
          graph[x][y] = 1
           
          for a in range(4):
            dfs(x+dx[a], y+dy[a])

n, m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      result += 1
      dfs(i, j)

print(result)