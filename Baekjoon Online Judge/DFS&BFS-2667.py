def dfs(i, j):
  if 0<=i<N and 0<=j<N:
    if array[i][j] == 1:
        array[i][j] = 0
        count[sum] += 1
           
        for a in range(4):
          dfs(i+dx[a], j+dy[a])

N = int(input())
count = [0] * ((N**2//2+1)+1)
array = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sum = 0
for i in range(N):
  for j in range(N):
    if array[i][j] == 1:
      sum += 1
      dfs(i, j)

count.sort()
print(sum)
for i in count:
  if i != 0:
    print(i)