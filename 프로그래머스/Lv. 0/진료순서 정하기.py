def solution(emergency):
        
    rank_dict = {item: rank for rank, item in enumerate(sorted(emergency, reverse=True), start=1)}

    return [rank_dict[item] for item in emergency]
