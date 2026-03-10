def parse(tokens):
    tokens.pop(0)
    
    children = []
    while tokens[0] != '#':
        children.append(parse(tokens))
        
    tokens.pop(0)
    return children


def change_brackets(tree):
    return sorted('(' + ''.join(change_brackets(child)) + ')' for child in tree)
    

def main():
    
    n = int(input())
    
    for _ in range(n):
        tree1 = list(input().split())
        tree2 = list(input().split())
    
        tokens1 = parse(tree1)
        tokens2 = parse(tree2)
        
        result1 = change_brackets(tokens1)
        result2 = change_brackets(tokens2)
        
        if result1 == result2:
            print("The two trees are isomorphic.")
        else:
            print("The two trees are not isomorphic.")
        
              
if __name__ == "__main__":
    main()
