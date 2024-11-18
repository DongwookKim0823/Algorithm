from itertools import permutations

def solution(user_id, banned_id):
    
    def check_correct(list1, list2):
        
        for item1, item2 in zip(list1, list2):
            if len(item1) != len(item2):
                return False
            
            for a, b in zip(item1, item2):

                if b == '*':
                    continue

                if a != b:
                    return False
        return True
    
    valid_cases = set()
    for perm in permutations(user_id, len(banned_id)):
        if check_correct(perm, banned_id):
            valid_cases.add(tuple(sorted(perm)))

    return len(valid_cases)
