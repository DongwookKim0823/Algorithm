from collections import defaultdict

def solution(rows, columns, queries):
    answer = []
    current_state = defaultdict(int)
    
    for query in queries:
        edge = []
        value = []
        
        x1, y1, x2, y2 = query
        for y in range(y1, y2):
            edge.append((x1, y))
            value.append(current_state.get((x1, y), (x1 - 1) * columns + y))
        for x in range(x1, x2):
            edge.append((x, y2))
            value.append(current_state.get((x, y2), (x - 1) * columns + y2))
        for y in range(y2, y1, -1):
            edge.append((x2, y))
            value.append(current_state.get((x2, y), (x2 - 1) * columns + y))
        for x in range(x2, x1, -1):
            edge.append((x, y1))
            value.append(current_state.get((x, y1), (x - 1) * columns + y1))
            
        answer.append(min(value))
        
        for key, value in zip(edge, [value[-1]] + value[:-1]):
            current_state[key] = value
    
    return answer
