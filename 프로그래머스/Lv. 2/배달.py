from collections import defaultdict, deque

def solution(N, road, K):
    
    def bfs(start):
        visited = [float('inf')] * (N + 1)
        queue = deque([start])
        visited[start] = 0
        
        while queue:
            cur_node = queue.popleft()
            for next_node in road_dict[cur_node]:
                time = visited[cur_node] + time_dict[(cur_node, next_node)]
                
                if time <= K and visited[next_node] > time:
                    queue.append(next_node)
                    visited[next_node] = time
        
        return sum(1 for time in visited if time <= K)
                
        
    road_dict = defaultdict(list)
    time_dict = defaultdict(lambda: float('inf'))
    for i in road:
        a, b, time = i
        
        road_dict[a].append(b)
        road_dict[b].append(a)
        
        time_dict[(a, b)] = min(time_dict[(a, b)], time)
        time_dict[(b, a)] = min(time_dict[(b, a)], time)

    return bfs(1)
