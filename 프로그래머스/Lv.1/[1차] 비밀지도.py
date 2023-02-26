def solution(n, arr1, arr2):
    
    answer = []
    
    arr1_map = []
    for arr in arr1:
        arr1_map.append('0' * (n - len(bin(arr)[2:])) + str(bin(arr)[2:]) if len(bin(arr)[2:]) < n else bin(arr)[2:])
    
    arr2_map = []
    for arr in arr2:
        arr2_map.append('0' * (n - len(bin(arr)[2:])) + str(bin(arr)[2:]) if len(bin(arr)[2:]) < n else bin(arr)[2:])
        
    for i in range(n):
        real_layer = ''
        for j in range(n):
            real_layer += '#' if arr1_map[i][j] == '1' or arr2_map[i][j] == '1' else ' '
        answer.append(real_layer)
    
    return answer