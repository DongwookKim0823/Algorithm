def solution(s):

    temp = 0
    for i in s:
        if i == '(':
            temp += 1
        else:
            temp -= 1
        
        if temp < 0:
            return False
    
    if temp != 0:
        return False
        
    return True