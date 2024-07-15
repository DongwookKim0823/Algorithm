def knapsack(N, K, weights, values):

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, K + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N][K]


N, K = map(int, input().split())  # N: 물건 수, K: 버틸 수 있는 무게
weights = []
values = []

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

result = knapsack(N, K, weights, values)
print(result)
