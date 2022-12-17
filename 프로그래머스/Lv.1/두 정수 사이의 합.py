def solution(a, b):
    return sum(x for x in range(sorted([a, b])[0], sorted([a, b])[1] + 1))