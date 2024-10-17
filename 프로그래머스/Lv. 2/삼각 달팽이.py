def solution(n):
    
    cur_x, cur_y = 0, -1
    direction = 1
    current_num = 1
    roots = [[0 for _ in range(n)] for _ in range(n)]
    
    for move_count in range(n, 0 , -1):
        
        if direction % 3 == 1:  # 아래로
            for _ in range(move_count):
                cur_y += 1
                roots[cur_y][cur_x] = current_num
                current_num += 1
                
        elif direction % 3 == 2:  # 오른쪽
            for _ in range(move_count):
                cur_x += 1
                roots[cur_y][cur_x] = current_num
                current_num += 1
                
        else:  # 위로
            for _ in range(move_count):
                cur_x, cur_y = cur_x - 1, cur_y - 1
                roots[cur_y][cur_x] = current_num
                current_num += 1
        
        direction += 1
        
    answer = []
    for root in roots:
        for i in root:
            if i != 0:
                answer.append(i)
        
    return answer
