import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        p = input()
        n = int(input())
        array = input().rstrip()
        nums = deque(map(int, array[1:-1].split(','))) if array != '[]' else deque([])
        
        error = False
        reversed_state = False
        for operator in p:
            if operator == 'R':
                reversed_state = False if reversed_state else True
                continue
            
            if operator == 'D':
                if nums:
                    nums.pop() if reversed_state else nums.popleft()
                else:
                    error = True
        
        if error:
            print('error')
        else:
            print(str(list(reversed(nums))).replace(' ','') if reversed_state else str(list(nums)).replace(' ', ''))
