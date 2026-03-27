if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    
    answer = N
    for student_cnt in A:
        student_cnt -= B
        
        if student_cnt <= 0:
            continue
        
        answer += (student_cnt // C)
        if student_cnt % C > 0:
            answer += 1
        
    print(answer)
