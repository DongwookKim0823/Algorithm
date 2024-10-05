def solution(files):
    
    split_files = []
    for file in files:
        find_digit = False
        number_index = []
        for i in range(len(file)):
            if find_digit and not file[i].isdigit():
                break
            
            if file[i].isdigit():
                find_digit = True
                number_index.append(i)
                
        split_files.append((file[:number_index[0]], file[number_index[0]:number_index[-1]+1], file[number_index[-1]+1:]))
            
    split_files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    answer = [''.join(file) for file in split_files]
    
    return answer
