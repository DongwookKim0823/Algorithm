def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    return [-1] if len(answer) == 0 else sorted(answer)