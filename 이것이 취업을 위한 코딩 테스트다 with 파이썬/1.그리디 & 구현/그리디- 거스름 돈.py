import sys

while True:
  N = int(sys.stdin.readline().rstrip())
  if N%10 == 0:
    break
  else:
   continue

coin = [500, 100, 50, 10]
result = 0

for i in coin:
  result += N // i
  N %= i
  
print(result)