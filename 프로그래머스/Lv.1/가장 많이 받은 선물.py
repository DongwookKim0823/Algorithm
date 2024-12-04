from collections import defaultdict

def solution(friends, gifts):
    
    give_count = defaultdict(lambda: defaultdict(int))
    gift_point = defaultdict(lambda: defaultdict(int))
    for gift in gifts:
        give, take = gift.split()
        give_count[give][take] += 1
        
        gift_point[give]['give'] += 1
        gift_point[take]['take'] += 1
        
    for i in gift_point:
        gift_point[i]['point'] = gift_point[i]['give'] - gift_point[i]['take']
        
    result = defaultdict(int)
    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            if give_count[friends[i]][friends[j]] > give_count[friends[j]][friends[i]]:
                result[friends[i]] += 1
            elif give_count[friends[i]][friends[j]] < give_count[friends[j]][friends[i]]:
                result[friends[j]] += 1
            else:
                if gift_point[friends[i]]['point'] > gift_point[friends[j]]['point']:
                    result[friends[i]] += 1
                elif gift_point[friends[i]]['point'] < gift_point[friends[j]]['point']:
                    result[friends[j]] += 1
                    
    return 0 if len(result) == 0 else max(result.values())
