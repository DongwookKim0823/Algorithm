from itertools import combinations


if __name__ == "__main__":
    
    n, k = map(int, input().split())
    
    arr = set()
    for _ in range(n):
        arr.add(tuple(map(int, input().split())))
        
    answer = float('inf')
    for comb in combinations(arr, k):
        shelter = set(comb)
        house = arr - shelter
        
        cur_long_dist = 0
        for h in house:
            
            cur_short_dist = float('inf')
            for s in shelter:
                cur_short_dist = min(cur_short_dist, abs(s[0] - h[0]) + abs(s[1] - h[1]))
                
            cur_long_dist = max(cur_long_dist, cur_short_dist)
            
        answer = min(answer, cur_long_dist)
                
    print(answer)
    
