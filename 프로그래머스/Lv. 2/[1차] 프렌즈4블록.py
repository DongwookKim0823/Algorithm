def solution(m, n, board):
    board = [list(i) for i in board]
    
    def relocation(board):
        for j in range(n):
            remain_block = [board[i][j] for i in range(m) if board[i][j] != 0]
            remain_block = [0] * (m - len(remain_block)) + remain_block    
            for i in range(m):
                board[i][j] = remain_block[i]
                
                
    def count_remove_block(board):
        remove_block = 0
        for j in range(n):
            for i in range(m):
                if board[i][j] == 0:
                    remove_block += 1
                
        return remove_block
    
    
    while True:
        common_position_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    common_position_set.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
                
        for i, j in common_position_set:
            board[i][j] = 0
            
        relocation(board)
        
        if not common_position_set:
            break

    answer = count_remove_block(board)
    return answer
