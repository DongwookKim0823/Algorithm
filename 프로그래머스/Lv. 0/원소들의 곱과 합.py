import functools

def solution(num_list):
    return 1 if functools.reduce(lambda x, y: x * y, num_list) < sum(num_list) ** 2 else 0
