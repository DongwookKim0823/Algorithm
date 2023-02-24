def solution(participant, completion):
    
    participant_dic = {}
    for i in participant:
        if i in participant_dic:
            participant_dic[i] += 1
        else:
            participant_dic[i] = 1
            
    completion_dic = {}
    for i in completion:
        if i in completion_dic:
            completion_dic[i] += 1
        else:
            completion_dic[i] = 1
            
    if completion_dic.keys() == participant_dic.keys():
        for i in completion_dic.keys():
            if completion_dic[i] != participant_dic[i]:
                return i
    else:
        for i in participant_dic.keys():
            if i not in completion_dic.keys():
                return i