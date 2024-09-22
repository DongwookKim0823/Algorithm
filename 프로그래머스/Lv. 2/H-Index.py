def solution(citations):
    citations.sort(reverse=True)
    for num in range(min(len(citations), citations[0]), -1, -1):
        
        h_index = 0
        for citation in citations:
            if citation >= num:
                h_index += 1
            else:
                break
                
        if num <= h_index:
            return num
        
