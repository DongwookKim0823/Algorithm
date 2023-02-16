def solution(brown, yellow):
    
    length_list = []
    for width in range(1, yellow + 1):
        height = 0
        if yellow % width == 0:
            height = yellow // width
            if width >= height:
                length_list.append((width,height))
        else:
            continue

    for width, height in length_list:
        if width * 2 + height * 2 + 4 == brown:
            return [width + 2, height + 2]