import sys

n = int(input())

stack = []
sum = 0
for i in range(n):
  x = int(sys.stdin.readline().strip())

  if x == 0:
    stack.pop()
  else:
    stack.append(x)

for i in stack:
  sum += i

print(sum)