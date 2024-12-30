if __name__ == '__main__':
    
    def factorial(n):
        if n == 1:
            return 1
        
        return n * factorial(n - 1)
    
    n = int(input())
    
    if n == 0:
        print(0)
    else:
        count = 0
        for i, num in enumerate(str(factorial(n))[::-1], start=1):
            if num != '0':
                break
            
            count += 1
            
        print(count)
