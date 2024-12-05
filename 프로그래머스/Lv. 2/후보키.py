from itertools import combinations


def solution(relation):
    
    def check_possible(comb, relation):
        
        item_set = set()
        for item in relation:
            
            temp = list()
            for index in comb:
                temp.append(item[index])
                
            item_set.add(tuple(temp))

        return True if len(item_set) == row_count else False

    
    col_count = len(relation[0])
    row_count = len(relation)
    
    candidate = list()
    for i in range(1, col_count + 1):
        for comb in list(combinations(range(col_count), i)):
            if check_possible(comb, relation):
                candidate.append(set(comb))
                
    result = []
    for s in candidate:
        is_minimal = True
        for t in candidate:
            if t != s and t.issubset(s):
                is_minimal = False
                break
            
        if is_minimal:
            result.append(s)

    return len(result)
