def solution(s):
    
    min_length = float('inf')
    for increase in range(1, len(s) + 1):
        
        start = 0
        compress_list = []
        while start < len(s):
            compress = s[start : start + increase]
            if compress_list and compress_list[-1][0] == compress:
                compress_list[-1][1] += 1
            else:
                compress_list.append([compress, 1])
            start += increase
        
        compress_s = ''.join(f"{string}{count if count > 1 else ''}" for string, count in compress_list)
        min_length = min(min_length, len(compress_s))
        
    return min_length
