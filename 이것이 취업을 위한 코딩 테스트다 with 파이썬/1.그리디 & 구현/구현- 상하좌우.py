n = int(input())
path = list(map(str, input().split()))

s = [1, 1]

for i in path:

  if i == 'L':
    if s[1]-1<1:
      continue
    s[1] -= 1
  elif i == 'R':
    if s[1]+1>n:
      continue
    s[1] += 1
  elif i == 'U':
    if s[0]-1<1:
      continue
    s[0] -= 1
  elif i == 'D':
    if s[0]+1>n:
      continue
    s[0] += 1
print(s[0], s[1])