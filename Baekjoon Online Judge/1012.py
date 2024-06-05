def dfs(field, x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if field[y][x] == 1:
            field[y][x] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(field[0]) and 0 <= ny < len(field):
                    if field[ny][nx] == 1:
                        stack.append((nx, ny))


test_count = int(input())

for _ in range(test_count):
    # 변수 및 배열 초기화
    width, height, cabbage = map(int, input().split())
    field = [[0 for _ in range(width)] for _ in range(height)]
    earthworm = 0

    for _ in range(cabbage):
        x, y = map(int, input().split())
        field[y][x] = 1

    # 모든 필드 순회
    for y in range(height):
        for x in range(width):
            if field[y][x] == 1:
                earthworm += 1
                dfs(field, x, y)

    print(earthworm)
