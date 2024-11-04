import math

def solution(picks, minerals):
    
    mineral_dict = {"diamond": 25, "iron": 5, "stone": 1}
    
    points = []
    temp = [0, 0, 0]
    for index, mineral in enumerate(minerals):
        
        if index != 0 and index % 5 == 0:
            points.append(temp)
            temp = [0, 0, 0]
        
        if mineral == "diamond":
            temp[0] += 1
        elif mineral == "iron":
            temp[1] += 1
        elif mineral == "stone":
            temp[2] += 1
            
    if sum(temp) > 0:
        points.append(temp)
    
    if len(points) > sum(picks):
        points = points[:sum(picks)]
        
    points.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    tools = []
    for pick, energy in zip(picks, [25, 5, 1]):
        tools.extend([energy] * pick)

    result = 0
    for point, tool in zip(points, tools):
        
        mineral_list = []
        for count, energy in zip(point, [25, 5, 1]):
            mineral_list.extend([energy] * count)
            
        for mineral in mineral_list:
            result += math.ceil(mineral / tool)
            
    return result
