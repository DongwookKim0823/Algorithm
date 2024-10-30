def solution(places):
    
    def check_distance(place, i, j):
        
        # 인접한 자리
        if j > 0 and place[i][j - 1] == 'P':
            return False
        
        if i > 0 and place[i - 1][j] == 'P':
            return False
        
        if i < 4 and place[i + 1][j] == 'P':
            return False
        
        if j < 4 and place[i][j + 1] == 'P':
            return False

        # 대각선 자리
        if i > 0 and j > 0:
            if place[i - 1][j - 1] == 'P' and (place[i - 1][j] == 'O' or place[i][j - 1] == 'O'):
                return False
        
        if i > 0 and j < 4:
            if place[i - 1][j + 1] == 'P' and (place[i - 1][j] == 'O' or place[i][j + 1] == 'O'):
                return False
        
        if i < 4 and j < 4:
            if place[i + 1][j + 1] == 'P' and (place[i + 1][j] == 'O' or place[i][j + 1] == 'O'):
                return False
        
        if i < 4 and j > 0:
            if place[i + 1][j - 1] == 'P' and (place[i + 1][j] == 'O' or place[i][j - 1] == 'O'):
                return False
            
        # 두 칸 떨어진 자리
        if j > 1 and place[i][j - 2] == 'P' and place[i][j - 1] != 'X':
            return False
        
        if i > 1 and place[i - 2][j] == 'P' and place[i - 1][j] != 'X':
            return False
        
        if i < 3 and place[i + 2][j] == 'P' and place[i + 1][j] != 'X':
            return False
        
        if j < 3 and place[i][j + 2] == 'P' and place[i][j + 1] != 'X':
            return False
        
        
        return True
    
    
    result = []
    for place in places:
        flag = True
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not check_distance(place, i, j):
                    flag = False
                    break
                    
            if flag == False:
                break
                
        result.append(1) if flag == True else result.append(0)
                        
    return result
