def solution(skill, skill_trees):
    answer = 0
    
    possible_skills = []
    for i in range(len(skill) + 1):
        possible_skills.append(skill[:i])
        
    for skill_tree in skill_trees:
        filtered_skill = ""
        for element in skill_tree:
            if element in skill:
                filtered_skill += element
        
        if filtered_skill in possible_skills:
            answer += 1
                
    return answer
