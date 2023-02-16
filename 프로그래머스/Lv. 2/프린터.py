from collections import deque

def solution(priorities, location):

    queue = deque()
    for i in zip(priorities, range(len(priorities))):
        queue.append(i)

    answer = 0
    while queue:
        pri, loc = queue.popleft()
        
        insert = False
        for temp_pri, temp_loc in queue:
            if temp_pri > pri:
                insert = True
                break

        if insert == True:
            queue.append((pri, loc))
        else:
            answer += 1
            if location == loc:
                return answer