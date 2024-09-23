def solution(board, h, w):
    count = 0
    color = board[h][w]
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]  
        
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]):
            if color == board[nh][nw]:
                count += 1
    
    return count
