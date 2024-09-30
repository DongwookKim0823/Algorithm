def solution(order):
    
    index = 0
    stack = []
    truck = []
    
    for num in range(1, len(order)+1):
        if num != order[index]:
            stack.append(num)
        else:
            truck.append(num)
            index += 1
            
            while stack and stack[-1] == order[index]:
                truck.append(stack.pop())
                index += 1

    return len(truck)

