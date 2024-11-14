def solution(A, B):
    
    a = sorted(A, reverse=True)
    b = sorted(B, reverse=True)
    
    count = 0
    for _ in range(len(A)):
        if a[-1] < b[-1]:
            a.pop()
            b.pop()
            count += 1
        else:
            b = [b.pop()] + b
            
    return count
