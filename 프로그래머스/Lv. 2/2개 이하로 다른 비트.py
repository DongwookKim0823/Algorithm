def solution(numbers):
    
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            num_bin = '0' + bin(number)[2:]
            for i in range(len(num_bin) - 2, -1, -1):
                if num_bin[i:i+2] == '01':
                    answer.append(int(num_bin[:i] + '10' + num_bin[i+2:], 2))
                    break
            
    return answer
