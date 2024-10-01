def solution(land):
    for layer in range(1, len(land)):
        for point in range(4):
            land[layer][point] += max(land[layer-1][index] for index in range(4) if point != index)
        
    return max(land[-1])
