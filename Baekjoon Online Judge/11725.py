from collections import defaultdict, deque


def find_parents(tree):
    parent_node = {}

    queue = deque([1])
    parent_node[1] = None

    while queue:
        current = queue.popleft()
        for neighbor in tree[current]:
            if neighbor not in parent_node:
                parent_node[neighbor] = current
                queue.append(neighbor)

    return parent_node


if __name__ == '__main__':
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    result_dict = find_parents(tree)

    for i in range(2, N+1):
        print(result_dict[i])
