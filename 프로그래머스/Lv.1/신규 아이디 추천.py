stop_word = "~!@#$%^&*()=+[{]}:?,<>/"

def step1(new_id):
    new_id1 = ''
    for i in new_id:
        if i.isalpha():
            new_id1 += i.lower()
            continue
        new_id1 += i
    return new_id1

def step2(new_id):
    new_id2 = ''
    for i in new_id:
        if i not in stop_word:
            new_id2 += i
    return new_id2

def step3(new_id):
    new_id_list = list(new_id)
    for i in range(1, len(new_id_list)):
        if new_id_list[i - 1] == '.' and new_id_list[i] == '.':
            new_id_list[i - 1] = ''
    return ''.join(new_id_list)

def step4(new_id):
    return new_id.strip('.')

def step5(new_id):
    if len(new_id) == 0:
        new_id += 'a'
    return new_id

def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    return new_id.rstrip('.')

def step7(new_id):
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

def solution(new_id):
    new_id1 = step1(new_id)
    new_id2 = step2(new_id1)
    new_id3 = step3(new_id2)
    new_id4 = step4(new_id3)
    new_id5 = step5(new_id4)
    new_id6 = step6(new_id5)
    new_id7 = step7(new_id6)

    return new_id7