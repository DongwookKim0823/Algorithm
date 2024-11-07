def solution(n, s):
    
    if n > s:
        return [-1]

    quotient, remainder = divmod(s, n)
    
    return [quotient] * (n - remainder) + [quotient + 1] * remainder
