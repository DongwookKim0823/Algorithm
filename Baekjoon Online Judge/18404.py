from collections import deque


def bfs(targets, x, y, N):
    possible_dirs = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    queue = deque([[(x, y), 0]])
    visited = set()
    result = [0] * len(targets)
    while queue:
        current, count = queue.popleft()
        if 0 in result:
            if current in targets and result[targets.index(current)] == 0:
                result[targets.index(current)] = count

            for nx, ny in possible_dirs:
                next_x = current[0] + nx
                next_y = current[1] + ny
                if 0 < next_x <= N and 0 < next_y <= N and (next_x, next_y) not in visited:
                    queue.append([(current[0] + nx, current[1] + ny), count + 1])
                    visited.add((next_x, next_y))
    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    x, y = map(int, input().split())
    targets = [tuple(map(int, input().split())) for _ in range(M)]

    result = bfs(targets, x, y, N)

    print(*result)
