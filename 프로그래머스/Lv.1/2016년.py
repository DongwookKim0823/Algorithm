def solution(a, b):
    month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    day = 0
    for i in range(1, a): day += month[i]
    day += b
    
    return days[day % 7 - 1]