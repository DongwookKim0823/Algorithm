from collections import defaultdict

def solution(n, results):
    
    def dfs(win_graph, node, visited, visited_nodes):
        visited[node] = True
        
        for next_node in win_graph[node]:
            if not visited[next_node]:
                visited_nodes.add(next_node)
                dfs(win_graph, next_node, visited, visited_nodes)
        
    
    rank = [0] * (n + 1)
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in results:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)
        
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        visited_nodes = set()
        dfs(win_graph, i, visited, visited_nodes)
        win_graph[i] = visited_nodes
        
        visited = [False] * (n + 1)
        visited_nodes = set()
        dfs(lose_graph, i, visited, visited_nodes)
        lose_graph[i] = visited_nodes
        
    count = 0
    for i in range(1, n + 1):
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:
            count += 1
            
    return count
