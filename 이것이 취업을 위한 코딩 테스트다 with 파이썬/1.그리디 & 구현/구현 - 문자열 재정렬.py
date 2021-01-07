string = input()
result = []
num = 0

for i in string:
    if 0 <=  ord(i) - ord('0') <= 9:
        num += ord(i) - ord('0')
    else:
        result.append(i)

result.sort()

if num != 0:
    result.append(str(num))
    
print("".join(result))