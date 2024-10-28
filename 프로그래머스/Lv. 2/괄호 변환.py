def solution(w):
    
    def split_to_uv(w):        
        stack = []
        index = 0
        for element in w:
            if not stack:
                stack.append(element)
            else:
                stack.append(element) if stack[-1] == element else stack.pop()
            
            index += 1
            
            if not stack:
                break
                 
        return w[:index], w[index:]
    
    
    def is_correct_bracket(u):
        value = 0
        for element in u:
            value = value + 1 if element == '(' else value - 1
            
            if value < 0:
                return False
            
        return True
    
    
    def reverse_bracket(u):
        temp = ''
        for element in u:
            temp = temp + ')' if element == '(' else temp + '('
            
        return temp
                
    
    def recursive_func(w):
        if not w:
            return ''
        
        u, v = split_to_uv(w)
        
        if is_correct_bracket(u):
            return u + recursive_func(v)
        else:
            temp = '(' + recursive_func(v) + ')' + reverse_bracket(u[1:-1])
            return temp


    return recursive_func(w)
