if __name__ == '__main__':
    
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
        
    left, right = 0, max(trees)
    
    while left <= right:    
        mid = (left + right) // 2 
        if m <= sum(max(tree - mid, 0) for tree in trees):
            left = mid + 1
        else:
            right = mid - 1
            
    print(right)
