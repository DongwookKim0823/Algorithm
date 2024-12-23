import sys
import heapq

input = sys.stdin.readline

if __name__ == '__main__':
    heap = []
    
    for _ in range(int(input())):
        num = int(input())
        
        if num > 0:
            heapq.heappush(heap, -1 * num)
        elif num == 0:
            print(heapq.heappop(heap) * -1 if heap else 0)
