n = int(input())
array = list(map(int, input().split()))
array.sort()

sum = 0
i = 0
while n>0:
  sum += array[i] * n 
  i += 1
  n -= 1

print(sum)