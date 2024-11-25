def solution(a):
    a.append(a[-1] - a[-2]) if a[-2] < a[-1] else a.append(a[-1] * 2)
    return a
