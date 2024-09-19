def solution(wallet, bill):
    count = 0
    wallet.sort()
    
    while True:
        bill.sort()
        
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
            
        bill[1] = bill[1] // 2
        count += 1
          
    return count
