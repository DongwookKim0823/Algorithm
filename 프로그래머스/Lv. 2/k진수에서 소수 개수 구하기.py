import math

def solution(n, k):
    
    def change_to_k(n, k):
        result = ''
        while n > 0:
            result = str(n % k) + result
            n //= k          
        return result
    
    def is_prime_num(num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
        
    count = 0
    transformed_num = change_to_k(n, k)
    for num_str in transformed_num.split('0'):
        if num_str and num_str != '1':
            if is_prime_num(int(num_str)):
                count += 1

    return count
