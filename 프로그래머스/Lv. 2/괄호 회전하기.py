def solution(s):
    
    def check_currect(s):
        stack = []
        for element in s:
            if element in '({[':
                stack.append(element)
            elif element in ')}]':
                if not stack:
                    return False
                top = stack.pop()
                if top == '(' and element != ')':
                    return False
                if top == '[' and element != ']':
                    return False
                if top == '{' and element != '}':
                    return False
        return len(stack) == 0
    
    currect_count = 0
    
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if check_currect(s):
            currect_count += 1

    return currect_count
