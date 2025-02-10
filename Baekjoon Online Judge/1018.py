if __name__ == '__main__':
    
    chess_board1 = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
    ]
    
    chess_board2 = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
    ]
    
    def check_count(i, j, board):
        
        count1 = 0
        count2 = 0
        
        for a in range(8):
            for b in range(8):
                if board[i + a][j + b] != chess_board1[a][b]:
                    count1 += 1
                if board[i + a][j + b] != chess_board2[a][b]:
                    count2 += 1
        
        return min(count1, count2)
                
    
    m, n = map(int, input().split())
    board = [input() for _ in range(m)]
    
    result = float('inf')
    for i in range(m - 7):
        for j in range(n - 7):
            result = min(check_count(i, j, board), result)
    
    print(result)
