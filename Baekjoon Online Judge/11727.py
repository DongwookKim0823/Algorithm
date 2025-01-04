import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    
    if n == 1:
        print(1)
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 3
        
        for count, index in enumerate(range(3, n + 1), start=1):
            dp[index] = (dp[index - 1] + 2 * dp[index - 2]) % 10007
        
        print(dp[n])
