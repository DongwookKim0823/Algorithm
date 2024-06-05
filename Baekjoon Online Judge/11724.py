import sys


def dfs(field, start, visited):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for index, value in enumerate(field[node]):
                if value == 1 and not visited[index]:
                    stack.append(index)


if __name__ == '__main__':
    input = sys.stdin.readline
    count = 0
    n, m = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    field = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        field[u][v] = 1
        field[v][u] = 1

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(field, i, visited)
            count += 1

    print(count)
