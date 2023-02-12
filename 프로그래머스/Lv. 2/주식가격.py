def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        temp = -1
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                temp = j - i
                break
        if temp == -1:
            temp = len(prices) -1  - i
        answer.append(temp)

    answer.append(0)
    
    return answer