import math


def check_prime_num(num):
    if num == 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True


if __name__ == '__main__':
    
    start, end = map(int, input().split())
    
    for i in range(start, end + 1):
        if check_prime_num(i):
            print(i)
