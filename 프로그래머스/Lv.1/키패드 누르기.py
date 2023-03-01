def solution(numbers, hand):
    answer = ''
    
    num_loc = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2], 4 : [1, 0], 5 : [1, 1], 6 : [1, 2], 7 : [2, 0], 8 : [2, 1], 9 : [2, 2], 0 : [3, 1], '*' : [3, 0], '#' : [3, 2]}
    
    now_left_loc = '*'
    now_right_loc = '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            now_left_loc = number
        elif number in [3, 6, 9]:
            answer += 'R'
            now_right_loc = number
        else:
            left_hand_dist = abs(num_loc[number][0] - num_loc[now_left_loc][0]) + abs(num_loc[number][1] - num_loc[now_left_loc][1])
            right_hand_dist = abs(num_loc[number][0] - num_loc[now_right_loc][0]) + abs(num_loc[number][1] - num_loc[now_right_loc][1])
            
            if left_hand_dist == right_hand_dist:
                if hand == "left":
                    answer += 'L'
                    now_left_loc = number
                else:
                    answer += 'R'
                    now_right_loc = number
            elif left_hand_dist < right_hand_dist:
                answer += 'L'
                now_left_loc = number
            else:
                answer += 'R'
                now_right_loc = number
                
    return answer