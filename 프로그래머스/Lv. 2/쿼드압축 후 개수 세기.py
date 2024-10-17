def solution(arr):
    
    def recursive_func(x, y, size):
        
        cur_sum = 0
        for ny in range(y, y + size):
            for nx in range(x, x + size):
                cur_sum += arr[ny][nx]
                
        if cur_sum == size * size:
            nonlocal count_1
            count_1 += 1
        elif cur_sum == 0:
            nonlocal count_0
            count_0 += 1
        else:
            recursive_func(x, y, size // 2)
            recursive_func(x + size // 2, y, size // 2)
            recursive_func(x, y + size // 2, size // 2)
            recursive_func(x + size // 2, y + size // 2, size // 2)
        
    count_0, count_1 = 0, 0
    recursive_func(0, 0, len(arr))
    
    return [count_0, count_1]
