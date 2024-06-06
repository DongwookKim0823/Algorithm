import sys


def bfs(graph, visited, start):
    from collections import deque
    queue = deque()
    queue.append((start, -1))
    visited[start] = True

    while queue:
        current_node, parent_node = queue.popleft()

        for neighbor_node in graph[current_node]:
            if not visited[neighbor_node]:
                queue.append((neighbor_node, current_node))
                visited[neighbor_node] = True
            elif neighbor_node != parent_node:
                return 0
    return 1


def count_tree(graph):
    count = 0
    visited = [False for _ in range(len(graph) + 1)]

    for node in graph:
        if not visited[node]:
            count += bfs(graph, visited, node)
    return count


def main():
    input = sys.stdin.readline
    case = 0

    while True:
        case += 1
        count = 0
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        graph = {}
        for i in range(1, n + 1):
            graph[i] = []

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        count = count_tree(graph)

        if count == 0:
            print(f"Case {case}: No trees.")
        elif count == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {count} trees.")


if __name__ == '__main__':
    main()
