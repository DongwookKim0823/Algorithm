from collections import defaultdict


if __name__ == '__main__':
    
    for _ in range(int(input())):
        
        clothes = defaultdict(list)
        for _ in range(int(input())):
            name, kind = input().split()
            clothes[kind].append(name)
            
        result = 1
        for kind, names in clothes.items():
            result *= len(names) + 1
            
        print(result - 1)
