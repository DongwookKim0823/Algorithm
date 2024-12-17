import sys

input = sys.stdin.readline

if __name__ == '__main__':
    num_set = set()
    for _ in range(int(input())):
        command = input().split()
        
        if len(command) == 1:
            action = command[0]
        else:
            action, x = command[0], int(command[1])

        if action == 'add':
            num_set.add(x) 
        elif action == 'remove':
            num_set.discard(x)
        elif action == 'check':
            print(1 if x in num_set else 0)
        elif action == 'toggle':
            num_set.remove(x) if x in num_set else num_set.add(x)
        elif action == 'all':
            num_set = set(range(1, 21))
        elif action == 'empty':
            num_set = set()
            
