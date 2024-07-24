from collections import deque


def bfs(field, x, y, R, C):

    queue = deque([(x, y)])

    sheep = 0
    wolf = 0
    while queue:
        cx, cy = queue.popleft()
        if field[cy][cx] == "#" or field[cy][cx] == "c":
            continue
        if field[cy][cx] == "o":
            sheep += 1
        if field[cy][cx] == "v":
            wolf += 1

        field[cy][cx] = "c"

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= ny < R and 0 <= nx < C and field[ny][nx] != "c" and field[ny][nx] != "#":
                queue.append((nx, ny))

    return sheep, wolf


if __name__ == "__main__":
    R, C = map(int, input().split())

    field = []
    for _ in range(R):
        field.append(list(input()))

    total_sheep = 0
    total_wolf = 0
    for y in range(R):
        for x in range(C):
            if field[y][x] == "#" or field[y][x] == "c":
                continue
            sheep, wolf = bfs(field, x, y, R, C)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

    print(total_sheep, total_wolf)
