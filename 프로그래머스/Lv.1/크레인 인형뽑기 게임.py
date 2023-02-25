def solution(board, moves):
    
    box = []
    pop_cnt = 0
    
    for move in moves:
        
        for layer in board:
            if layer[move - 1] == 0:
                continue
            else:
                doll = layer[move - 1]
                layer[move - 1] = 0
                box.append(doll)
                break
                
        if len(box) > 1:
            if box[-1] == box[-2]:
                box.pop()
                box.pop()
                pop_cnt += 2
    
    return pop_cnt