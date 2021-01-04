import sys

n = int(input())
for _ in range(n):
  line = sys.stdin.readline().rstrip()
  buffer = 0

  for i in line:
    if i == '(':
      buffer += 1
    else:
      buffer -= 1

      if buffer < 0:
        break

  if buffer == 0: print("YES")
  else: print("NO")