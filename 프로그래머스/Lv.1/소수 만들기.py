from itertools import combinations

def solution(nums):
    
    answer = 0
    for combination in combinations(nums, 3):
        combi_sum = sum(combination)
        flag = True
        for j in range(2, combi_sum):
            if combi_sum % j == 0:
                flag = False
                break
        if flag == True: answer += 1
            
    return answer