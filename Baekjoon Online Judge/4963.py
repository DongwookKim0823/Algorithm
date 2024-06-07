import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def bfs(array, x, y):
    array[y][x] = 0

    for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(array[0]) and 0 <= ny < len(array):
            if array[ny][nx] == 1:
                bfs(array, nx, ny)


def count_island(array):
    count = 0

    for y in range(len(array)):
        for x in range(len(array[0])):
            if array[y][x] == 1:
                bfs(array, x, y)
                count += 1

    return count


def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        grid = [list(map(int, input().split())) for _ in range(h)]
        print(count_island(grid))


if __name__ == "__main__":
    main()
