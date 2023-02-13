word_dic = []
alphabet = ['A', 'E', 'I', 'O', 'U']

def rec_func(length, temp_word):
    if len(temp_word) == length:
        word_dic.append(temp_word)
    else:
        for i in alphabet:
            temp_word += i
            rec_func(length, temp_word)
            temp_word = temp_word[:-1]

def solution(word):
    for i in range(1, 6):
        rec_func(i, '')
    
    word_dic.sort()
    
    return word_dic.index(word) + 1