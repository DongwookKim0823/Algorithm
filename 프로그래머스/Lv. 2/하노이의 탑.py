def solution(n):
    def hanoi(num, fm, to, other):
        if num == 0:
            return
        hanoi(num - 1, fm, other, to)
        route.append([fm, to])
        hanoi(num - 1, other, to, fm)
        
    route = []
    hanoi(n, 1, 3, 2)
    return route
