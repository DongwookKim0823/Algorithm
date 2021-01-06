import sys
from collections import deque  

q = deque()

for _ in range(int(input())):
  line = sys.stdin.readline().rstrip()
  c = line.split()

  if c[0] == 'push':
    q.appendleft(c[1])
    continue
  elif c[0] == 'pop':
    print(q.pop() if q else -1)
    continue
  elif c[0] == 'size':
    print(len(q))
    continue
  elif c[0] == 'empty':
    print(0 if q else 1)
    continue
  elif c[0] == 'front':
    print(q[-1] if q else -1)
    continue
  elif c[0] == 'back':
    print(q[0] if q else -1)
    continue