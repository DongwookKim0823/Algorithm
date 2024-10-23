def solution(data, ext, val_ext, sort_by):
    
    col_dict = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3,
    }
    
    return sorted([i for i in data if i[col_dict[ext]] < val_ext], key=lambda x: x[col_dict[sort_by]])
