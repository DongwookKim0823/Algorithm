from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    bridge = deque([0 for _ in range(bridge_length)])
    arrived_truck = []
    truck_cnt = len(truck_weights)
    truck_weights = deque(truck_weights)
    whole_weight = sum(truck_weights)
    
    while len(arrived_truck) != truck_cnt:
        
        if len(truck_weights) == 0:
            second += bridge_length
            break
        
        temp_arrived_truck = bridge.popleft()
        if temp_arrived_truck != 0: 
            arrived_truck.append(temp_arrived_truck)
        bridge.append(0)
        
        if len(truck_weights) != 0 and whole_weight - sum(arrived_truck) - sum(truck_weights)  + truck_weights[0] <= weight:
            bridge[-1] = truck_weights.popleft()
        
        second += 1

    return second
