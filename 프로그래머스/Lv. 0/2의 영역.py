def solution(arr):
    a = [i for i, n in enumerate(arr) if n == 2]
    return [-1] if a == [] else arr[a[0]:a[-1]+1]
