def solution(players, callings):
    
    player_dict = {}
    order_dict = {}
    for index, player in enumerate(players, start=1):
        player_dict[player] = index
        order_dict[index] = player
        
    for calling in callings:
        index = player_dict[calling]
        pre_player = order_dict[index-1]

        player_dict[calling], player_dict[pre_player] = player_dict[pre_player], player_dict[calling]
        order_dict[index-1], order_dict[index] = order_dict[index], order_dict[index-1]
    
    return [value for key, value in sorted(order_dict.items())]
