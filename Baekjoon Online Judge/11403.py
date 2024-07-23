from collections import deque


def bfs(start_node, graph, N):
    visited = [0] * N
    queue = deque([start_node])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)

    return visited


if __name__ == '__main__':
    N = int(input())

    graph = {}
    for i in range(N):
        graph[i] = []
        for index, j in enumerate(list(map(int, input().split()))):
            if j > 0:
                graph[i].append(index)

    result = []
    for start_node in range(N):
        result.append(bfs(start_node, graph, N))

    for row in result:
        print(' '.join(map(str, row)))
