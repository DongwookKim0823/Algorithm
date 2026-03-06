def main():
    arr = input()
    bomb = list(input())
    
    stack = []    
    for a in arr:
        stack.append(a)
        if len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
            del stack[-len(bomb):]
            
    if not stack:
        return "FRULA"
        
    answer = ''.join(stack)
    return answer


if __name__ == "__main__":
    answer = main()
    print(answer)
