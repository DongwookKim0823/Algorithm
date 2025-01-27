from collections import deque


def func(a, b):
    
    queue = deque([(a, '')])
    visited = [False] * 10000
    visited[a] = True
    
    while queue:
        cur_a, commands = queue.popleft()
        
        if cur_a == b:
            return commands
        
        d = cur_a * 2 % 10000
        if not visited[d]:
            queue.append((d, commands + 'D'))
            visited[d] = True
            
        s = 9999 if cur_a == 0 else cur_a - 1
        if not visited[s]:
            queue.append((s, commands + 'S'))
            visited[s] = True
            
        l = cur_a % 1000 * 10 + cur_a // 1000
        if not visited[l]:
            queue.append((l, commands + 'L'))
            visited[l] = True
        
        r = cur_a % 10 * 1000 + cur_a // 10
        if not visited[r]:
            queue.append((r, commands + 'R'))
            visited[r] = True


if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        
        print(func(a, b))
