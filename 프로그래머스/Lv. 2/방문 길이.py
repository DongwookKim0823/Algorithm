def solution(dirs):
    
    dir_dict = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    
    current = (0, 0)
    moved_roots = []
    
    for dir in dirs:
        next_x = dir_dict[dir][0] + current[0]
        next_y = dir_dict[dir][1] + current[1]
        
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            moved_root = sorted(((current[0], current[1]), (next_x, next_y)))
            if moved_root not in moved_roots:
                moved_roots.append(moved_root)

            current = (next_x, next_y)
        
    return len(moved_roots)
