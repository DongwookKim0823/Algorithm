def solution(numbers, target):
    
    def recursive(index, total):
        nonlocal count
        if index == 0:
            if target == total:
                count += 1
            return
        
        recursive(index - 1, total + numbers[index - 1])
        recursive(index - 1, total - numbers[index - 1])
    
    count = 0
    recursive(len(numbers), 0)
    
    return count
