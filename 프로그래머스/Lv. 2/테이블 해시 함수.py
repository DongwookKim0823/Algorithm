def solution(data, col, row_begin, row_end):
    
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    result = 0
    for index in range(row_begin - 1, row_end):
        result ^= sum(num % (index + 1) for num in data[index])

    return result
