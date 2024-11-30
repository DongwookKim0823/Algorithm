def solution(myString, pat):
    return sum([1 for i in range(len(myString)) if myString[i:i+len(pat)] == pat])
