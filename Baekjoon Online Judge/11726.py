if __name__ == '__main__':
    n = int(input())

    dy = [0] * 1001
    dy[1], dy[2], dy[3] = 1, 2, 3

    for i in range(4, 1001):
        dy[i] = (dy[i-1] + dy[i-2]) % 10007

    print(dy[n])
