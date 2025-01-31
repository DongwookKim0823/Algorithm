from collections import deque

if __name__ == '__main__':
    deque = deque([])
    for _ in range(int(input())):
        command = input()
        
        if command.startswith('push_front'):
            x = command.split()[1]
            deque.appendleft(x)
        elif command.startswith('push_back'):
            x = command.split()[1]
            deque.append(x)
        elif command.startswith('pop_front'):
            if deque:
                print(deque.popleft())
            else:
                print(-1)
        elif command.startswith('pop_back'):
            if deque:
                print(deque.pop())
            else:
                print(-1)
        elif command.startswith('size'):
            print(len(deque))
        elif command.startswith('empty'):
            print(0 if deque else 1)
        elif command.startswith('front'):
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif command.startswith('back'):
            if deque:
                print(deque[-1])
            else:
                print(-1)
