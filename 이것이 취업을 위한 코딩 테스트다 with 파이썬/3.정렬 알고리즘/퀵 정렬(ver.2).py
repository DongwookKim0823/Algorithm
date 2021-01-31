array = list(map(int, input().split()))

def quick_sort(array):
  
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left = [i for i in tail if i<=pivot]
  right = [i for i in tail if i>pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))