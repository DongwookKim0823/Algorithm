if __name__ == "__main__":
    N = int(input())
    M = N // 2
    
    ABLITY = []
    for _ in range(N):
        ABLITY.append(list(map(int, input().split())))
    
    def calc(a_list, b_list):
        a_sum = 0
        b_sum = 0
        
        for i in a_list:
            for j in a_list:
                if i == j:
                    continue
                
                a_sum += ABLITY[i][j]
                
        for i in b_list:
            for j in b_list:
                if i == j:
                    continue
                
                b_sum += ABLITY[i][j]
                
        
        return abs(a_sum - b_sum)
        
    
    answer = float("inf")
    def dfs(n, a_list, b_list):
        global answer
        
        if answer == 0:
            return
        
        if n == N:
            if len(a_list) == len(b_list):
                answer = min(answer, calc(a_list, b_list))
            return
        
        dfs(n + 1, a_list + [n], b_list)
        dfs(n + 1, a_list, b_list + [n])
    
    dfs(0, [], [])
    
    print(answer)
