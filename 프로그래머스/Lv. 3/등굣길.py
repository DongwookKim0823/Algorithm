def solution(m, n, puddles):
    
    routes = [[0 for _ in range(m)] for _ in range(n)]
    
    for x, y in puddles:
        routes[y-1][x-1] = -1
    
    routes[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if routes[i][j] == -1:
                continue
            
            if j > 0 and routes[i][j-1] != -1:
                routes[i][j] += routes[i][j-1]
                    
            if i > 0 and routes[i-1][j] != -1:
                routes[i][j] += routes[i-1][j]
                    
            routes[i][j] %= 1000000007

    return routes[n-1][m-1]
