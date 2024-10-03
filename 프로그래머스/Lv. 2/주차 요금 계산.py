from collections import defaultdict
import math


def solution(fees, records):
    records = list(map(lambda x: (int(x[0].split(':')[0]) * 60 + int(x[0].split(':')[1]), x[1], x[2]), map(lambda x: x.split(), records)))
    fee_dict = defaultdict(int)
    
    for i in range(len(records)):
        if records[i][2] == 'OUT':
            continue
        
        car_num = records[i][1]
        for j in range(i+1, len(records)):
            if car_num == records[j][1] and records[j][2] == 'OUT':
                fee_dict[records[i][1]] += records[j][0] - records[i][0]  
                break
        else:
            fee_dict[records[i][1]] += 23*60+59 - records[i][0]
    
    answer = []
    for i in sorted(fee_dict):
        if fee_dict[i] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((fee_dict[i] - fees[0]) / fees[2]) * fees[3])
                
    return answer
