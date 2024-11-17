def solution(n, stations, w):
    
    cur_station = 1
    full_length = 2 * w + 1
    
    necessary_station = 0
    for station in stations:
        empty_station = station - cur_station - w
        a, b = divmod(empty_station, full_length)
        
        necessary_station += a
        if b > 0:
            necessary_station += 1
                        
        cur_station = station + w + 1

    if cur_station <= n:
        empty_station = n - cur_station + 1
        a, b = divmod(empty_station, full_length)
        
        necessary_station += a
        if b > 0:
            necessary_station += 1

    return necessary_station
