def solution(bandage, health, attacks):
    max_health = health
    
    attack_dict = {key: value for key, value in attacks}
    
    usage_time, recovery_amount, extra_amount = bandage
    accumulate_count = 0
    for i in range(1, attacks[-1][0] + 1):
        
        if i in attack_dict:
            accumulate_count = 0
            health -= attack_dict[i]
            
            if health <= 0:
                return -1
        
        else:
            accumulate_count += 1
            health += recovery_amount
            
            if accumulate_count == usage_time:
                health += extra_amount
                accumulate_count = 0
                
            if health > max_health:
                health = max_health
            
    return health
