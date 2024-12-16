if __name__ == '__main__':
    depth = int(input())
    
    triangle = [[]]
    for cur_depth in range(1, depth + 1):
        temp_list = list(map(int, input().split()))
        triangle.append(temp_list)
        
        if cur_depth > 1:
            for index in range(cur_depth):
                if index == 0:
                    triangle[cur_depth][index] += triangle[cur_depth - 1][index]
                elif index == cur_depth - 1:
                    triangle[cur_depth][index] += triangle[cur_depth - 1][index - 1]
                else:
                    triangle[cur_depth][index] += max(triangle[cur_depth - 1][index], triangle[cur_depth - 1][index - 1])
                    
    print(max(triangle[depth]))
    
