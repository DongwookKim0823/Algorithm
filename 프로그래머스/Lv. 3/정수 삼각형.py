def solution(triangle):
    
    for layer in range(1, len(triangle)):
        for index in range(len(triangle[layer])):
            if index == 0:
                triangle[layer][index] += triangle[layer - 1][index]
            elif index == len(triangle[layer]) - 1:
                triangle[layer][index] += triangle[layer - 1][index - 1]
            else:
                triangle[layer][index] += max(triangle[layer - 1][index], triangle[layer - 1][index - 1])
                
    return max(triangle[-1])
