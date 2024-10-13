from collections import defaultdict, deque

def solution(n, edge):
    
    def bfs(start):
        visited = [-1] * (n + 1)
        queue = deque([(start, 0)])
        visited[start] = 0
        max_distance = 0
        count = 0
        
        while queue:
            cur_node, distance = queue.popleft()
            
            if distance > max_distance:
                max_distance = distance
                count = 1
            elif distance == max_distance:
                count += 1
            
            for next_node in graph[cur_node]:
                if visited[next_node] == -1:
                    queue.append((next_node, distance + 1))
                    visited[next_node] = distance + 1
                    
        return count
    
    graph = defaultdict(list)
    for i in edge:
        a, b = i
        
        graph[a].append(b)
        graph[b].append(a)
        
    return bfs(1)
