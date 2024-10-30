import heapq

def solution(n, k, enemys):
    
    max_heap = []
    
    for rnd, enemy in enumerate(enemys, start=1):
    
        heapq.heappush(max_heap, -enemy)
        n -= enemy
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(max_heap)
                k -= 1
            else:
                return rnd - 1
        
    return rnd
