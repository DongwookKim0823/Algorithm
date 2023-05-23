import copy

def solution(want, number, discount):
    answer = 0
    
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    for start in range(len(discount) - 9):
        
        temp_dic = copy.deepcopy(want_dic)
        flag = True
        for index in range(10):
            if discount[start + index] not in temp_dic:
                flag = False
                break
                
            temp_dic[discount[start + index]] -= 1
            
        for value in temp_dic.values():
            if value != 0:
                flag = False
                break
                
        if flag is True:
            answer += 1
            
    return answer
