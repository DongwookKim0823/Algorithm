if __name__ == '__main__':
    n = int(input())
    m = int(input())
    INF = 1_000_000_000
    
    costs = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        costs[i][i] = 0
    
    for _  in range(m):
        a, b, cost = map(int, input().split())
        costs[a - 1][b - 1] = min(cost, costs[a - 1][b - 1])
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
                    
    for cost in costs:
        for idx in range(len(cost)):
            if cost[idx] == INF:
                cost[idx] = 0
        print(*cost)
