n = input()
x = int(n[1])
y = ord(n[0]) - 96

count = 0

for i in range(1,5):
    if i == 1:
        if 1<=x-2 and 1<=y-1:
            count += 1
        if 1<=x-2 and 8>=y+1:
            count += 1
    elif i == 2:
        if 8>=y+2 and 8>=x+1:
            count += 1
        if 8>=y+2 and 1<=x-1:
            count += 1
    elif i == 3:
        if 8>=x+2 and 1<=y-1:
            count += 1
        if 8>=x+2 and 8>=y+1:
            count += 1
    elif i == 4:
        if 1<=y-2 and 8>=x+1:
            count += 1
        if 1<=y-2 and 1<=x-1:
            count += 1
        
print(count)