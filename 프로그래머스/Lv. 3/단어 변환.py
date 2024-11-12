def solution(begin, target, words):
    
    def can_change(word1, word2):
        count = 0
        for a, b in zip(word1, word2):
            if a != b:
                count += 1
        
        return True if count == 1 else False 
                
    def dfs(cur_word, visited, distance):
        if cur_word == target:
            distance.append(visited.count(True))
            return
        
        for index, next_word in enumerate(words):
            if can_change(cur_word, next_word) and visited[index] == False:
                visited[index] = True
                dfs(next_word, visited, distance)
                visited[index] = False
                
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    distance = []
    dfs(begin, visited, distance)

    return min(distance)
