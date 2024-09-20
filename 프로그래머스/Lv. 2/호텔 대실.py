def solution(book_time):
    time_tuple = []
    for start, end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        time_tuple.append((start_h * 60 + start_m, end_h * 60 + end_m))

    time_tuple.sort(key=lambda x: (x[0], x[1]))
    book_sequence = []
    for time in time_tuple:
        if book_sequence:
            for sequence in book_sequence:
                possible_start_time = sequence[-1][1] + 10
                
                if possible_start_time <= time[0]:
                    sequence.append(time)
                    break
            else:
                book_sequence.append([time])
        else:
            book_sequence.append([time])

    return len(book_sequence)
