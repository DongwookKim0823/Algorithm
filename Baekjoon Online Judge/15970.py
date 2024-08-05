from collections import defaultdict

if __name__ == '__main__':
    N = int(input())

    color_dic = defaultdict(list)
    for _ in range(N):
        point, color = map(int, input().split())
        color_dic[color].append(point)

    length_sum = 0
    for color in color_dic.keys():
        points = sorted(color_dic[color])
        for index in range(len(points)):
            if index == 0:
                length_sum += points[index + 1] - points[index]
            elif index == len(points) - 1:
                length_sum += points[index] - points[index - 1]
            else:
                length_sum += min(points[index + 1] - points[index], points[index] - points[index - 1])

    print(length_sum)
