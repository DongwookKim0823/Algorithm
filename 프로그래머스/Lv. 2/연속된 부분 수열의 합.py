def solution(sequence, k):
    
    left = right = 0
    min_length = float('inf')
    cur_sum = sequence[0]

    answer = []
    while right < len(sequence):
        
        if cur_sum < k:
            right += 1
            if right < len(sequence):
                cur_sum += sequence[right]
        elif cur_sum > k:
            cur_sum -= sequence[left]
            left += 1
        else:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                answer = [left, right]
                
            cur_sum -= sequence[left]
            left += 1
            
    return answer
