def solution(num_string):
    
    num_dic = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    answer = ''
    temp_str = ''
    for i in num_string:
        if i.isdigit():
            if temp_str == '':
                answer += i
            else:
                answer += num_dic[temp_str]
                temp_str= ''
                answer += i
        else:
            temp_str += i
            if temp_str in num_dic:
                answer += num_dic[temp_str]
                temp_str = ''
                
    return int(answer)