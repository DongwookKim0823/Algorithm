array = []
for i in range(int(input())):
  array.append(int(input()))

k = 0
for i in array:
  if k < abs(i):
    k = abs(i)

count = [0] * (k*2+1)

array.sort()
for i in array:
  if i < 0:
    i = i*(-2) - 1
  else:
    i *= 2
  count[i] += 1

result = []
for i in range(len(count)):
  if count[i] == max(count):
    if i % 2 == 0:
      result.append(i//2)
    else:
      result.append((i+1)//(-2))
result.sort()

print(int(round(sum(array)/len(array), 0)))
print(array[len(array)//2])

if len(result) == 1:
  print(result[0])
else:
  print(result[1])

print(array[-1]-array[0])