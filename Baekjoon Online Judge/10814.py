if __name__ == '__main__':
    
    member = []
    for i in range(int(input())):       
        temp = input()
        age = int(temp.split()[0])
        name = temp.split()[1]
        
        member.append((age, name, i))
        
    member.sort(key=lambda x: (x[0], x[2]))
        
    for m in member:
        print(m[0], m[1])
