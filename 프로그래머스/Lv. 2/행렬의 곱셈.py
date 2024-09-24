def solution(arr1, arr2):
    
    def multiplication(array1, array2):
        
        num = 0
        for i in range(len(array1)):
            num += array1[i] * array2[i]
            
        return num
        
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(arr1)):      
        for j in range(len(arr2[0])):
            temp = []
            for h in range(len(arr2)):
                temp.append(arr2[h][j])

            answer[i][j] = multiplication(arr1[i], temp)
            
    return answer
