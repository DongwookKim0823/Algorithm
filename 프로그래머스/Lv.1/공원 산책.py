def solution(park, routes):
    
    cur_dir = [[i, j] for i in range(len(park)) for j in range(len(park[0])) if park[i][j] == 'S'][0]

    for route in routes:
        direction, distance = route.split()[0], int(route.split()[1])
        i, j = cur_dir
        
        is_possible = True
        if direction == 'E':
            for increase in range(1, distance + 1):
                if j + increase >= len(park[0]) or park[cur_dir[0]][cur_dir[1] + increase] == 'X':
                    is_possible = False
                    break
            else:
                cur_dir[1] += increase
        elif direction == 'W':
            for increase in range(1, distance + 1):
                if j - increase < 0 or park[cur_dir[0]][cur_dir[1] - increase] == 'X':
                    is_possible = False
                    break
            else:
                cur_dir[1] -= increase
        elif direction == 'S':
            for increase in range(1, distance + 1):
                if i + increase >= len(park) or park[cur_dir[0] + increase][cur_dir[1]] == 'X':
                    is_possible = False
                    break
            else:
                cur_dir[0] += increase
        elif direction == 'N':
            for increase in range(1, distance + 1):
                if i - increase < 0 or park[cur_dir[0] - increase][cur_dir[1]] == 'X':
                    is_possible = False
                    break
            else:
                cur_dir[0] -= increase
                
    return cur_dir
