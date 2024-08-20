from collections import defaultdict, deque


if __name__ == '__main__':
    def bfs(relation, user):
        queue = deque([(user, 0)])
        visited = [user]
        depth_sum = 0

        while queue:
            current_user, count = queue.popleft()
            depth_sum += count

            for next_user in relation[current_user]:
                if next_user not in visited:
                    queue.append((next_user, count + 1))
                    visited.append(next_user)

        return depth_sum


    n, m = map(int, input().split())
    relation = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    result = [0] * (n + 1)
    for user in range(1, n + 1):
        result[user] = bfs(relation, user)

    result = result[1:]
    print(result.index(min(result)) + 1)
