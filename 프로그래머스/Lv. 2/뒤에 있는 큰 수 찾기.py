def solution(numbers):
    
    stack = []
    answer = []
    
    for number in numbers[::-1]:
        
        while True:
            if stack:
                if stack[-1] <= number:
                    stack.pop()
                else:
                    answer.append(stack[-1])
                    stack.append(number)
                    break
            else:
                stack.append(number)
                answer.append(-1)
                break
            
    return answer[::-1]
