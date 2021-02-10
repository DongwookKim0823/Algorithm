def binary_search(key, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if array[mid] == key:
    return mid
  elif array[mid] < key: 
    return binary_search(key, mid+1, end)
  else:
    return binary_search(key, start, mid-1)

array = list(map(int, input().split()))
key = int(input())

result = binary_search(key, 0, len(array)-1)

if result == None:
  print(str(key)+'��(��) �������� �ʽ��ϴ�.')
else:
  print('key�� ��ġ : ' + str(result+1))