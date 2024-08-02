from collections import deque


def minimum_move(size, start, target):
    if start == target:
        return 0

    possible_dir = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

    queue = deque([[start, 0]])
    visited = set()
    while queue:
        current_location, move_count = queue.popleft()
        current_x, current_y = current_location

        for x, y in possible_dir:
            if (0 <= current_x + x < size and 0 <= current_y + y < size) and (current_x + x, current_y + y) not in visited:
                if (current_x + x, current_y + y) == target:
                    return move_count + 1

                queue.append([[current_x + x, current_y + y], move_count + 1])
                visited.add((current_x + x, current_y + y))


if __name__ == '__main__':
    test_count = int(input())
    for _ in range(test_count):
        size = int(input())
        start = tuple(map(int, input().split()))
        target = tuple(map(int, input().split()))

        result = minimum_move(size, start, target)
        print(result)
