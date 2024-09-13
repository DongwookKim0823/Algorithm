def solution(n, left, right):
    array = []
    for index in range(left, right + 1):
        i = index // n
        j = index % n
        array.append(max(i + 1, j + 1))
        
    return array
