def solution(n):
    temp = []
    for i in n:
        temp.append(i)
        if len(temp) >= 2:
            if temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
    
    if len(temp) == 0:
        return 1
    else:
        return 0