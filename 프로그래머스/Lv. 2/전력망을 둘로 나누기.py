from collections import defaultdict, deque


def solution(n, wires):
    
    def bfs(line_dict, start):
        
        visited = [False for _ in range(n + 1)]
        queue = deque([start])
        visited[start] = True
        count = 1
        
        while queue:
            cur_num = queue.popleft()
            
            for num in line_dict[cur_num]:
                if not visited[num]:
                    queue.append(num)
                    visited[num] = True
                    count += 1
                    
        return count
    
    
    diff = float('inf')
    for i in range(len(wires)):
        remain_line = wires[:i] + wires[i+1:]
        
        line_dict = defaultdict(list)
        for line in remain_line:
            line_dict[line[0]].append(line[1])
            line_dict[line[1]].append(line[0])   

        count = bfs(line_dict, 1)
        cand_diff = abs(count - (n - count))
            
        diff = min(diff, cand_diff)

    return diff
