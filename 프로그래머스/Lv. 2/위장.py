def solution(clothes):

    answer = 1

    clothes_dict = {}
    for i in clothes:
        if i[1] in clothes_dict:
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 1

    for num in clothes_dict.values():
        answer *= (num + 1)
    
    return answer - 1