from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    
    if (queue1_sum + queue2_sum) % 2 != 0:
        return -1
    
    max_operations = len(queue1) * 3
        
    count = 0
    while count < max_operations:
        if queue1_sum > queue2_sum:
            poped_value = queue1.popleft()
            queue1_sum -= poped_value
            queue2_sum += poped_value
            queue2.append(poped_value)
        elif queue2_sum > queue1_sum:
            poped_value = queue2.popleft()
            queue2_sum -= poped_value
            queue1_sum += poped_value
            queue1.append(poped_value)
        else:
            return count
        count += 1
    
    return -1
