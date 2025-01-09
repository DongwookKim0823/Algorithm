def solution(arr, queries):
    
    result = []
    for query in queries:
        s, e, k = query
        
        num = -1
        for i in sorted(arr[s:e + 1]):
            if i > k:
                num = i
                break
                
        result.append(num)
    
    return result
