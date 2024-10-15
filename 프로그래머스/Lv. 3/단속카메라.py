def solution(routes):
    
    routes.sort(key=lambda x: x[1])
    
    pivot = routes[0][1]
    count = 1
    for route in routes:
        if pivot in range(route[0], route[1] + 1):
            continue
            
        pivot = route[1]
        count += 1
         
    return count
