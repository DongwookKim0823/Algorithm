if __name__ == '__main__':

    dp = [0, 0] * 41
    dp[0], dp[1], dp[2] = [1, 0], [0, 1], [1, 1]
    for i in range(3, 41):
        dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*dp[n])
