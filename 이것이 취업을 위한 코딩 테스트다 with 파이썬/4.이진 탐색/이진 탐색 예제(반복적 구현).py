def binary_search(key, start, end):

  while True:

    mid = (start + end) // 2

    if start <= end:
      if array[mid] == key:
        return mid
      elif array[mid] < key:
        start = mid + 1
      else:
        end = mid - 1
    else:
      return None

array = list(map(int, input().split()))
key = int(input())

result = binary_search(key, 0, len(array)-1)

if result == None:
  print('key�� �������� �ʽ��ϴ�.')
else:
  print('key�� ��ġ: '+ str(result+1))