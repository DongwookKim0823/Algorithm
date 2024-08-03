from collections import defaultdict


def dfs(tree, node, target, visited, count):
    if node == target:
        return count

    if node not in visited:
        visited.add(node)

        for neighbor in tree[node]:
            if neighbor not in visited:
                result = dfs(tree, neighbor, target, visited, count + 1)
                if result != -1:
                    return result

    return -1


if __name__ == '__main__':
    n = int(input())
    target_a, target_b = map(int, input().split())
    m = int(input())
    tree = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = set()
    result = dfs(tree, target_a, target_b, visited, 0)

    print(result)
