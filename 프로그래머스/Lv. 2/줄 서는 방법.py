import math


def solution(n, k):
    numbers = list(range(1, n + 1))
    result = []
    k -= 1
    
    for i in range(n, 0, -1):
        factorial_value = math.factorial(i - 1)
        index = k // factorial_value
        result.append(numbers.pop(index))
        k %= factorial_value
    
    return result
