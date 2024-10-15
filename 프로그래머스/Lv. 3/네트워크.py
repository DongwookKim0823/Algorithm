from collections import defaultdict


def solution(n, computers):
    
    def dfs(node, visited):
        visited[node] = True
        for next_node in range(n):
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node, visited)
                
    visited = [False] * n
    network_count = 0
    
    for node in range(n):
        if not visited[node]:
            dfs(node, visited)
            network_count += 1
    
    return network_count
