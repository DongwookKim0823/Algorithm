import sys

s = sys.stdin.readline().rstrip()
array = list(map(int, s))
result = array[0]

for i in array[1:]:
  if i < 2:
    result += i
  elif result == 0:
    result += 1
    result *= i
  else:
    result *= i

print(result)