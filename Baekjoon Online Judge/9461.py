if __name__ == '__main__':
    
    dp = [0] * 101
        
    for idx, num in enumerate([1, 1, 1, 2, 2], start=1):
        dp[idx] = num
        
    for idx in range(6, 101):
        dp[idx] = dp[idx - 1] + dp[idx - 5]
    
    for _ in range(int(input())):
        n = int(input()) 
        print(dp[n])
