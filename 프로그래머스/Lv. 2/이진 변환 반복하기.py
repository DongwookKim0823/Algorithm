def binary(num):
    global cnt
    string = ''
    while True:
        a = int(num / 2)
        b = int(num % 2)
        string = str(b) + string

        if a != 0:
            num = a
        else:
            break

    cnt += 1
    return string

def solution(s):

    length = 0
    deleted = 0
    while s != '1':
        length = len(s)
        s = s.replace('0', '')
        deleted += length - len(s)
        s = binary(len(s))
        
    return [cnt, deleted]

cnt = 0