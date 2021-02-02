def dfs(main, visited, V):
  visited[V] = True
  result.append(V)

  for i in main:
    if i[0] == V and visited[i[1]] == False:
      dfs(main, visited, i[1])
    elif i[1] == V and visited[i[0]] == False:
      dfs(main, visited, i[0])

N = int(input())
visited = [False] * (N+1)

main = []
result = []

for _ in range(int(input())):
  x,y = map(int, input().split())
  if x>y:
    x,y = y,x
  main.append([x,y])

main.sort(key = lambda x : (x[0], x[1]))

dfs(main, visited, 1)

print(len(result)-1)