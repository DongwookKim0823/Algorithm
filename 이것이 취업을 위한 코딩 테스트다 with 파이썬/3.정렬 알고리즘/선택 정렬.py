list = list(map(int, input().split()))

for i in range(len(list)):
  smallest = i
  for j in range(i+1, len(list)):
    if list[j] < list[smallest]:
      smallest = j
  list[i], list[smallest] = list[smallest], list[i]
print(list)