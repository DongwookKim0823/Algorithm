def solution(sequence):
    
    def max_subarray_sum(arr):
        current_max = arr[0]
        cur_sum = arr[0]
        
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            cur_sum = max(cur_sum, current_max)
            
        return cur_sum
    
    sequence1 = []
    sequence2 = []
    
    num = 1
    for i in sequence:
        sequence1.append(i * num)
        num = -1 if num == 1 else 1
    
    num = -1
    for i in sequence:
        sequence2.append(i * num)
        num = -1 if num == 1 else 1
    
    return max(max_subarray_sum(sequence1), max_subarray_sum(sequence2))
