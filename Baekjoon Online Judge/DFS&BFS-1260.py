from collections import deque

def dfs(main, visited, V):

  visited[V] = True
  print(V, end = ' ')

  for i in main:
      if i[0] == V and visited[i[1]] == False:
        visited[i[1]] = True
        dfs(main, visited, i[1])
      elif i[1] == V and visited[i[0]] == False:
        visited[i[0]] = True
        dfs(main, visited, i[0])

def bfs(main, visited, V):

  queue = deque([V])
  visited[V] = True

  while queue:
    x = queue.popleft()
    print(x, end = ' ')

    for i in main:
      if i[0] == x and visited[i[1]] == False:
        queue.append(i[1])
        visited[i[1]] = True
      elif i[1] == x and visited[i[0]] == False:
        queue.append(i[0])
        visited[i[0]] = True

N, M, V = map(int, input().split())

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

main = []

for _ in range(M):
  x, y = map(int, input().split())
  if x>y:
    x,y = y,x
  main.append((x,y))

main.sort(key = lambda x : (x[0], x[1]))

dfs(main, dfs_visited, V)
print()
bfs(main, bfs_visited, V)