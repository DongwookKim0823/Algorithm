def solution(n, words):
    answer = [0, 0]

    temp = [words[0]]
    for i in range(1, len(words)):
        
        if words[i] not in temp and temp[-1][-1] == words[i][0]:
            temp.append(words[i])
            continue

        answer[0] = i % n +1
        answer[1] = i // n + 1

        break
            
    return answer