from collections import defaultdict, deque


def find_connection(network):
    visited = set()
    queue = deque([1])
    visited.add(1)

    while queue:
        node = queue.popleft()

        for neighbor in network[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return len(visited) - 1


if __name__ == '__main__':
    node = int(input())
    connect = int(input())

    network = defaultdict(list)
    for _ in range(connect):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    result = find_connection(network)

    print(result)
