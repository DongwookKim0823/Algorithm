if __name__ == '__main__':
    
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]
    
    result = []
    for a in range(n):
        
        count = 1
        for b in range(n):
            
            if a == b:
                continue
            
            if people[a][0] < people[b][0] and people[a][1] < people[b][1]:
                count += 1
                
        result.append(count)
        
    print(*result)
