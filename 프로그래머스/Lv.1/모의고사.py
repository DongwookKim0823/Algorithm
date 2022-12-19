def solution(answers):
    student1 = [1, 2, 3, 4, 5] * (10000 // 5)
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10)
    students_score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == student1[i]: students_score[0] += 1
        if answers[i] == student2[i]: students_score[1] += 1
        if answers[i] == student3[i]: students_score[2] += 1
    
    answer = []
    for i in range(len(students_score)):
        if students_score[i] == max(students_score):
            answer.append(i + 1)
            
    return answer