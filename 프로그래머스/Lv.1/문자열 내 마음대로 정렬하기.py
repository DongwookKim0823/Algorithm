def solution(strings, n):
        
    temp = [(i, element, element[n]) for i, element in enumerate(strings)]
    temp.sort(key = lambda x : (x[1]))  
    temp.sort(key = lambda x : (x[2]))
    
    return [i[1] for i in temp]