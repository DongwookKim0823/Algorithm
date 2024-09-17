def solution(board):
    possible_win_comb = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)},
    ]
                   
    o_positions = set()
    x_positions = set()
    
    o_count = 0
    x_count = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_positions.add((i, j))
                o_count += 1
            if board[i][j] == 'X':
                x_positions.add((i, j))
                x_count += 1

    if o_count < x_count or o_count - x_count > 1:
        return 0
    
    o_win = False
    x_win = False
    
    for possible_win in possible_win_comb:        
        if possible_win <= o_positions:
            o_win = True
        if possible_win <= x_positions:
            x_win = True

        if o_win and x_win:
            return 0
    
    if o_win and o_count != x_count + 1:
        return 0
    
    if x_win and o_count != x_count:
        return 0
        
    return 1
