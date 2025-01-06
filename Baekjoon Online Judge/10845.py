import sys
from collections import deque

input = sys.stdin.readline


if __name__ == '__main__':
    
    queue = deque([])
    for _ in range(int(input())):
        
        command = input().rstrip().split()
        
        if len(command) == 2:
            command, num = command
        else:
            command = command[0]
            
        if command == 'push':
            queue.append(num)
        elif command == 'pop':
            print(queue.popleft() if queue else -1)
        elif command == 'size':
            print(len(queue))
        elif command == 'empty':
            print(0) if queue else print(1)
        elif command == 'front':
            print(queue[0] if queue else -1)
        elif command == 'back':
            print(queue[-1] if queue else -1)
