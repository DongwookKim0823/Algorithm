import sys
from collections import defaultdict


input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    num_dict = defaultdict(int)
    name_dict = defaultdict(str)
    
    for index in range(1, N + 1):
        name = input().rstrip()
        num_dict[index] = name
        name_dict[name] = index
        
    for _ in range(M):
        question = input().rstrip()
        
        if question.isdigit():
            print(num_dict[int(question)])
        else:
            print(name_dict[question])
        
