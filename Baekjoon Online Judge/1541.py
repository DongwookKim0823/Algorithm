if __name__ == '__main__':
    
    num = []
    operator = []
    
    temp = ''
    for i in input():
        if i.isdigit():
            temp += i
        else:
            num.append(int(temp))
            operator.append(i)
            temp = ''
    else:
        num.append(int(temp))

    while '+' in operator:
        index = operator.index('+')
        operator.pop(index)
        
        num[index] = num[index] +  num[index + 1]
        num.pop(index + 1)
        
    print(num[0] - sum(num[1:]) if len(num) > 1 else num[0])
