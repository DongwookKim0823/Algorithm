import heapq

def solution(n, works):
    
    if sum(works) < n:
        return 0
    
    heap = []
    for work in works:
        heapq.heappush(heap, work * -1)

    for _ in range(n):
        item = heapq.heappop(heap)
        heapq.heappush(heap, item + 1)
    
    return sum(map(lambda x: x * x, heap))
