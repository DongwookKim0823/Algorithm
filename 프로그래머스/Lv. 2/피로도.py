def solution(k, dungeons):
    
    def dfs(visited, remain, count):
        nonlocal max_count
        max_count = max(max_count, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and remain >= dungeons[i][0]:
                visited[i] = True
                dfs(visited, remain - dungeons[i][1], count + 1)
                visited[i] = False
    
    max_count = 0
    visited = [False for _ in range(len(dungeons))]
    dfs(visited, k, 0)
    
    return max_count
