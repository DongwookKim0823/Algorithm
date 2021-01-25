array = list(map(int, input().split()))

for i in range(1, len(array)):
  for j in reversed(range(i)):
    if array[j] > array[i]:
      array[i], array[j] = array[j], array[i]
      i -= 1
    else:
      break
       
print(array)