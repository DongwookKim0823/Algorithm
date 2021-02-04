import sys

N = int(input())

array = []
for i in range(N):
  array.append(int(sys.stdin.readline().strip()))

plus = []
minus = []
for i in array:
  if i > 0:
    plus.append(i)
  else:
    minus.append(i)

plus.sort(reverse=True)
minus.sort()

result = []

if len(plus) == 1:
  result.append(plus[0])
elif len(plus) > 1:
  for i in range(len(plus)//2):
    x = i*2
    if plus[x] == 1 or plus[x+1] == 1:
      result.append(plus[x]+plus[x+1])
    else:
      result.append(plus[x]*plus[x+1])

  if len(plus)%2 == 1:
    result.append(plus[-1])

if len(minus) == 1:
  result.append(minus[0])
elif len(minus) > 1:
  for i in range(len(minus)//2):
    x = i*2
    result.append(minus[x]*minus[x+1])
  if len(minus)%2 == 1:
    result.append(minus[-1])

print(sum(result))