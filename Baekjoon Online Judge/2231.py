if __name__ == '__main__':
    def func(n):
        for i in range(1, n + 1):
        
            candidate, sum_num = i, i
            while i > 0:
                sum_num += i % 10
                i //= 10
            
            if sum_num == n:
                return candidate    
        return 0
    
    n = int(input())
    print(func(n))
