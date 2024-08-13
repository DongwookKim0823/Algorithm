if __name__ == '__main__':
    dp = [0] * 100001
    dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 1, 2, 2, 3, 3, 6, 6
    for index in range(8, 100001):
        dp[index] = (dp[index - 2] + dp[index - 4] + dp[index - 6]) % 1000000009

    for _ in range(int(input())):
        print(dp[int(input())])
