import heapq

def solution(operations):
    
    min_heap = []
    max_heap = []

    for operation in operations:
        operation, num = operation.split()[0], int(operation.split()[1])
        
        if operation == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -1 * num)
        else:
            if num == 1 and max_heap and min_heap:
                value = heapq.heappop(max_heap) * -1
                min_heap.remove(value)
            if num == -1 and max_heap and min_heap:
                value = heapq.heappop(min_heap)
                max_heap.remove(value * -1)
                
    return [heapq.heappop(max_heap) * -1, heapq.heappop(min_heap)] if max_heap else [0, 0]
