if __name__ == '__main__':
    num = int(input())

    dp = [([0] * 10) for _ in range(num + 1)]
    for j in range(10):
        dp[1][j] = 1

    for i in range(1, num + 1):
        dp[i][0] = 1

    for i in range(2, num + 1):
        for j in range(1, 10):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10007

    print(sum(dp[num]) % 10007)
