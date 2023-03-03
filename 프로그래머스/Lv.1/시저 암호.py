def solution(s, n):
    upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    answer = ''
    for i in s:
        if i in upper_case:
            answer += upper_case[(upper_case.index(i) + n) % 26]
        if i in lower_case:
            answer += lower_case[(lower_case.index(i) + n) % 26]
        if i == ' ':
            answer += ' '
    
    return answer