import sys

n = int(input())
buffer = []
for i in range(n):
    req = sys.stdin.readline().strip()
    if req == 'pop':
        if len(buffer) == 0:
            print(-1)
            continue
        else:
            print(buffer.pop())
            continue
    elif req == 'size':
        print(len(buffer))
        continue
    elif req == 'empty':
        if len(buffer) == 0:
            print(1)
            continue
        else:
            print(0)
            continue
    elif req == 'top':
        if len(buffer) == 0:
            print(-1)
            continue
        else:
             print(buffer[-1])
             continue
    else:
        buffer.append(req[5:])
        continue