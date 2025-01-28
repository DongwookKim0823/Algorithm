import heapq


def dijkstra(graph, start):
    distance = [float('inf')] * (n + 1)
    queue = []
    
    heapq.heappush(queue, (0, start))
    while queue:
        cur_distance, cur_node = heapq.heappop(queue)
        
        if cur_distance > distance[cur_node]:
            continue
        
        for cost, nxt_node in graph[cur_node]:
            acc_cost = cost + cur_distance
            
            if acc_cost < distance[nxt_node]:
                distance[nxt_node] = acc_cost
                heapq.heappush(queue, (acc_cost, nxt_node))
    
    return distance

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, weight = map(int, input().split())
        graph[a].append((weight, b))
        
    start, end = map(int, input().split())
        
    distance = dijkstra(graph, start)
    
    print(distance[end])
