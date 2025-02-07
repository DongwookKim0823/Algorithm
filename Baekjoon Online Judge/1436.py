if __name__ == '__main__':
    
    n = int(input())
    
    count = 0
    cur_num = 1
    while True:
        cur_num += 1
        
        if '666' in str(cur_num):
            count += 1
            
        if count == n:
            print(cur_num)
            break
