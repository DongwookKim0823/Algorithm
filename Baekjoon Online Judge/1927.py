import heapq
import sys

input = sys.stdin.read
data = input().split()

heap = []
for num in data[1:]:
    num = int(num)
    
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
