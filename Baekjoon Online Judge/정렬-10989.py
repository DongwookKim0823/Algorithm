import sys

N = int(sys.stdin.readline().strip())
count = [0] * 10001
for i in range(N):
  count[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
  if count[i] != 0:
    for _ in range(count[i]):
      print(i)