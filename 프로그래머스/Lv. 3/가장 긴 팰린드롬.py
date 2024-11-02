def solution(s):
    
    palindrome = 0
    for index in range(len(s)):
        
        increase = 0
        while 0 <= index - increase < len(s) and 0 <= index + increase + 1 < len(s):
            if s[index - increase] == s[index + increase + 1]:
                increase += 1
            else:
                break

        palindrome = max(increase * 2, palindrome)    
        
        increase = 0
        while 0 <= index - increase < len(s) and 0 <= index + increase < len(s):
            if s[index - increase] == s[index + increase]:
                increase += 1
            else:
                break

            palindrome = max(increase * 2 - 1, palindrome)

    return palindrome
