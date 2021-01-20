import sys

n = int(input())

list = []
for i in range(n):
  list.append(int(sys.stdin.readline().strip()))

list.sort()
for i in list:
  print(i, end='\n')