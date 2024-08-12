if __name__ == '__main__':
    dp = [0] * 1000001
    dp[1], dp[2], dp[3] = 1, 2, 4
    for index in range(4, 1000001):
        dp[index] = (dp[index - 3] + dp[index - 2] + dp[index - 1]) % 1000000009

    for _ in range(int(input())):
        print(dp[int(input())])
