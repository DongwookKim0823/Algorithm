if __name__ == '__main__':

    dp = [0] * 21
    dp[0], dp[1] = 0, 1
    for i in range(2, 21):
        dp[i] = dp[i - 1] + dp[i - 2]

    n = int(input())
    print(dp[n])