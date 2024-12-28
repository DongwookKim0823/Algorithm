if __name__ == '__main__':
    x = int(input())
    
    dp = [0] * (10 ** 6 + 1)
        
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, x + 1):
        
        temp = [dp[i - 1]]
        if i % 3 == 0:
            temp.append(dp[i // 3])
        if i % 2 == 0:
            temp.append(dp[i // 2])
            
        dp[i] = min(temp) + 1
            
    print(dp[x])
