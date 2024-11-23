def solution(my_string, m, c):
    return my_string if m == 1 and c == 1 else ''.join([string for index, string in enumerate(my_string) if (index % m) + 1 == c])
